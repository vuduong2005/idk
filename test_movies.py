import unittest
import csv
from  library import Movies, add_new_object, add_views, list_all

class TestMovies(unittest.TestCase):

    def setUp(self):
        # Clear the CSV file and Movies list before each test
        Movies.movies.clear()
        self.reset_csv()

    def reset_csv(self):
        # Reset the CSV file to a known state
        with open("movies.csv", mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "name", "author", "rating", "views"])
            # Optionally, add some initial test data
            writer.writerow([1, "Movie A", "Author A", 5, 50])

    def test_add_new_object(self):
        add_new_object("Movie A", "Author A", 5, 100)
        self.assertEqual(len(Movies.movies), 1)
        self.assertEqual(Movies.movies[0].name, "Movie A")
    
    def test_add_views(self):
        add_new_object("Movie B", "Author B", 3, 50)
        add_views(1)  # Add views to movie with ID 1
        self.assertEqual(Movies.movies[0].views, 51)
    
    def test_next_id(self):
        add_new_object("Movie C", "Author C", 4, 20)
        self.assertEqual(Movies.next_id(), 2)
    
    def test_get_movie_attr(self):
        add_new_object("Movie D", "Author D", 2, 30)
        movie = Movies.get_movie_attr(1)
        self.assertIsNotNone(movie)
        self.assertEqual(movie.name, "Movie D")
    
    def test_list_all(self):
        add_new_object("Movie E", "Author E", 1, 40)
        self.assertIn("Movie E", list_all())

if __name__ == '__main__':
    unittest.main()
