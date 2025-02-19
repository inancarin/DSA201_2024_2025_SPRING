if __name__ == "__main__":
    movies = set()
    f = open("movies.txt")
    for line in f.readlines():
        line = line.strip() # removes all leading and trailing whitespaces(" ", "\t", "\n")  
        info = line.split(", ")
        for movie in info[1:]:
            movie = movie.strip()
            """
            if movie not in movies:
                movies.add(movie)
            """
            movies.add(movie)

    f.close()
    for i in range(5):
        minMovie = min(movies)
        print(minMovie)
        movies.remove(minMovie)