from tkinter import scrolledtext as tkst # imports the scrolled-text function from tkinter as tkst
import tkinter as tk  # imports the tkinter module
import library as lib  # Import your lib module
from library import Movies  # Assuming library.py contains the Movies class

def set_text(text_area, content):  # Inserts content into the text_area
    text_area.delete("1.0", tk.END)  # The existing content is deleted
    text_area.insert(1.0, content)  # New content is then added

class CreateVideo:
    playlist = []
    def __init__(self, frame):
        self.frame = frame

        enter_lbl = tk.Label(frame, text="Enter Video Index:")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.input_txt = tk.Entry(frame, width=5)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        add_btn = tk.Button(frame, text="Add Video", command=self.add_video)
        add_btn.grid(row=0, column=2, sticky="E", padx=10, pady=10)

        play_list_btn = tk.Button(frame, text="Play Playlist", command=self.increment_play_count)
        play_list_btn.grid(row=0, column=3, sticky="W", padx=10, pady=10)

        clear_btn = tk.Button(frame, text="Clear Playlist", command=self.clear_playlist)
        clear_btn.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(frame, width=64, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.playlist_txt = tkst.ScrolledText(frame, width=64, height=12, wrap="none")
        self.playlist_txt.grid(row=1, column=2, columnspan=2, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(frame, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.list_videos_clicked()

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.update_playlist_display()  # Initialize the display for the playlist

    def add_video(self):
        entry = self.input_txt.get()
        movie = lib.get_name(entry)
        if isinstance(movie, lib.Movies) and entry not in self.playlist:
            self.playlist.append(movie)  # Store the movie object
            self.update_playlist_display()  # Update display
            self.status_lbl.configure(text="Movie added to playlist.")
        elif entry in self.playlist:
            self.status_lbl.configure(text="Video is already in the playlist.")
        else:
            self.status_lbl.configure(text="Video not in Library.")

    def increment_play_count(self):
        for movie in self.playlist:
            lib.add_views(movie.id)  # Increment views for the video
        self.update_playlist_display()  # Update the display with new view counts
        self.status_lbl.configure(text="Playlist played! Views updated.")
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        Movies.refresh_instances()  # Refresh instances from CSV
        self.load_movies()

    def update_playlist_display(self):
        # Prepare the display for the playlist with updated views
        view_count_display = "\n".join(
            f"{movie.id} - {movie.name} - {movie.author} - {movie.rating}"
            for movie in self.playlist
        )
        set_text(self.playlist_txt, view_count_display)  # Update the playlist display
        
    def clear_playlist(self):
        self.playlist.clear()
        self.status_lbl.configure(text="Playlist cleared!")
        set_text(self.playlist_txt, '')  # Clear the playlist display  
