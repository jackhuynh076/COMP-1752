import tkinter as tk
import video_library as lib

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", content)

class CreateVideoList:
    def __init__(self, window):
        window.geometry("750x350")
        window.title("Create Video List")

        self.Add_video_Play_list_btn = tk.Button(window, text="Add Video to Playlist", command=self.Add_video_Playlist_clicked)
        self.Add_video_Play_list_btn.grid(row=0, column=0, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=20)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        self.list_videos_btn = tk.Button(window, text="Play Videos", command=self.Play_video_Play_list)
        self.list_videos_btn.grid(row=0, column=2, padx=10, pady=10)

        self.reset_video_btn = tk.Button(window, text="Reset Playlist", command=self.reset_video_playlist)
        self.reset_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 12))
        self.status_lbl.grid(row=1, columnspan=4, padx=10, pady=10)

        self.play_counter = 0
        self.playlist = []

        self.playlist_txt = tk.Text(window, width=50, height=10)
        self.playlist_txt.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    def Add_video_Playlist_clicked(self):
        video_id = self.input_txt.get()
        name = lib.get_name(video_id)
        if name:
            self.playlist.append(video_id)
            self.update_playlist_display()
            self.status_lbl.configure(text=f"Added video {video_id} to playlist")
        else:
            self.status_lbl.configure(text=f"Video {video_id} not found!")

    def update_playlist_display(self):
        playlist_names = [lib.get_name(video_id) for video_id in self.playlist]
        set_text(self.playlist_txt, "\n".join(playlist_names))

    def Play_video_Play_list(self):
        if self.playlist:
            video_id = self.playlist[self.play_counter % len(self.playlist)]
            lib.play_video(video_id)
            self.play_counter += 1
            self.status_lbl.configure(text=f"Playing video...")
        else:
            self.status_lbl.configure(text="No videos to play")

    def reset_video_playlist(self):
        self.play_counter = 0
        self.playlist = []
        self.update_playlist_display()
        self.status_lbl.configure(text="Reset video playlist")

if __name__ == "__main__":
    root = tk.Tk()
    app = CreateVideoList(root)
    root.mainloop()
        
         


    
          


       

   
