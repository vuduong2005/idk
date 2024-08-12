import csv
import pandas as pd


class Movies:
    movies = []

    def __init__(self, id, name, author, rating=0, views=0):
        self.id = id
        self.name = name
        self.author = author
        self.rating = rating
        self.views = views
        Movies.movies.append(self)

    def __repr__(self):
        return f"{self.id} - {self.name} - {self.author} - {self.rating} - {self.views}"

    @classmethod
    def instantiate_from_csv(cls):
        with open("movies.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                 Movies(
                    id=int(item.get("ID")),
                    name=str(item.get("name")),
                    author=str(item.get("author")),
                    rating=str(item.get("rating")),
                    views=int(item.get("views"))
                )

    @classmethod
    def next_id(cls):
        if cls.movies:
            max_id = max(movie.id for movie in cls.movies)
            return max_id + 1
        else:
            return 1

    @classmethod
    def get_movie_attr(cls, id):
        for movie in cls.movies:
            if movie.id == id:
                return movie
    @classmethod
    def refresh_instances(cls):
        Movies.movies.clear()
        Movies.instantiate_from_csv()


Movies.instantiate_from_csv()



def add_new_object(arg1, arg2, arg3, arg4):
    new_id = Movies.next_id()
    Movies(new_id, arg1, arg2, arg3, arg4)
    # Rewrite data in CSV file
    with open("movies.csv", mode='a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow([new_id, arg1, arg2, arg3, arg4])


def list_all():
    output = ""
    output += "\n".join(map(str, Movies.movies))
    return output


view_list = []


'''
def add_views(entry):
    file = "movies.csv"
    df = pd.read_csv(file)
    global view_list
    view_list.append(entry)

    for movie_id in view_list:
        df.loc[df['ID'] == movie_id, "views"] += 1
    df.to_csv("movies.csv", index=False)
    view_list.clear()
    '''
def refresh_instances(cls):
    Movies.movies.clear()
    Movies.instantiate_from_csv()



def get_name(entry):
    try:
        id = int(entry)
        movie = Movies.get_movie_attr(id)
        if movie:
            return movie
        else:
            return "Video Not Found."
    except ValueError:
        return "Invalid ID. Please enter a valid ID."
    


def add_views(movie_id):
    file = "movies.csv"
    df = pd.read_csv(file)

    if movie_id in df['ID'].values:
        df.loc[df['ID'] == movie_id, 'views'] += 1
        df.to_csv(file, index=False)
    else:
        raise ValueError("Movie ID not found")

    # Ensure Movies class is updated after changing CSV
    Movies.refresh_instances()


