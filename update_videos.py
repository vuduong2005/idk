import tkinter as tk  # imports the tkinter module
import tkinter.scrolledtext as tkst # imports the scrolled-text function from tkinter as tkst
import csv
from library import Movies  # Assuming library.py contains the Movies class

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class UpdateVideo():
    def __init__(self, window):
        self.window = window
        window.title("Update Movies")
        window.geometry("600x500")

        # Movie List Label
        self.movie_list_label = tk.Label(window, text="Select Movie:")
        self.movie_list_label.pack(pady=10)

        # Scrollable Listbox for Movies
        self.movie_listbox = tk.Listbox(window, width=70, height=10)
        self.movie_listbox.pack(pady=10)
        self.load_movies()

        # New Rating Label and Entry
        self.rating_label = tk.Label(window, text="New Rating:")
        self.rating_label.pack(pady=10)

        self.rating_entry = tk.Entry(window, width=50)
        self.rating_entry.pack(pady=5)

        # Update Button
        self.update_button = tk.Button(window, text="Update Rating", command=self.update_rating)
        self.update_button.pack(pady=20)

        # Text Area to show feedback
        self.feedback_area = tkst.ScrolledText(window, width=70, height=10)
        self.feedback_area.pack(pady=10)

    def load_movies(self):
        self.movie_listbox.delete(0, tk.END)  # Clear existing items
        for movie in Movies.movies:
            self.movie_listbox.insert(tk.END, f"{movie.id} - {movie.name} - {movie.author} - {movie.rating} - {movie.views}")

    def update_rating(self):
        selected_index = self.movie_listbox.curselection()
        if not selected_index:
            feedback = "Please select a movie from the list."
            set_text(self.feedback_area, feedback)
            return
        
        selected_movie = Movies.movies[selected_index[0]]
        new_rating = self.rating_entry.get()

        if new_rating:
            selected_movie.rating = new_rating
            self.save_movies()
            Movies.refresh_instances()  # Refresh instances from CSV
            self.load_movies()  # Refresh the listbox to show updated ratings
            feedback = f"Updated '{selected_movie.name}' to new rating: {new_rating}"
        else:
            feedback = "Please enter a valid rating."

        set_text(self.feedback_area, feedback)

    def save_movies(self):
        with open("movies.csv", mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "name", "author", "rating", "views"])
            for movie in Movies.movies:
                writer.writerow([movie.id, movie.name, movie.author, movie.rating, movie.views])

