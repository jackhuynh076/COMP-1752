import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class UpdateVideos:
    def __init__(self, window):
        window.geometry("850x350")
        window.title("Update Videos")

        self.video_listbox = tk.Listbox(window)
        self.video_listbox.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        self.rating_label = tk.Label(window, text="Enter New Rating")
        self.rating_label.grid(row=0, column=1, padx=10, pady=10)

        self.rating_entry = tk.Entry(window)
        self.rating_entry.grid(row=0, column=2, padx=10, pady=10)

        self.update_button = tk.Button(window, text="Update Rating", command=self.update_rating)
        self.update_button.grid(row=0, column=3, padx=10, pady=10)

        self.video_details_lbl = tk.Label(window, text="Video Details:")
        self.video_details_lbl.grid(row=1, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.update_video_listbox()

    def update_video_listbox(self):
        videos = lib.list_all().splitlines()
        for video in videos:
            self.video_listbox.insert(tk.END, video)

    def update_rating(self):
        selected_index = self.video_listbox.curselection()
        if selected_index:
            selected_video_key = self.video_listbox.get(selected_index).split()[0]
            new_rating = self.rating_entry.get()
            if new_rating.isdigit():
                lib.set_rating(selected_video_key, int(new_rating))
                self.update_video_details_display(selected_video_key)

    def update_video_details_display(self, key):
        name = lib.get_name(key)
        director = lib.get_director(key)
        rating = lib.get_rating(key)
        self.video_details_lbl.config(text=f"Video: {name}, Director: {director}, Rating: {rating}")

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()  
    UpdateVideos(window)
    window.mainloop()






