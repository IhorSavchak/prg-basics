movie_titles = ["Inception", "The Matrix", "Interstellar", "The Godfather", "The Dark Knight"]

with open("movies.txt", "w") as file:
    for i in movie_titles:
        file.write(i + "\n")