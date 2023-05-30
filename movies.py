import re
import random


class Video:
    def __init__(self, title, year, genre, play_count):
        self.title = title
        self.year = year
        self.genre = genre
        self.play_count = play_count

    def play(self):
        self.play_count += 1


class Movie(Video):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'{self.title} {self.year}'


class Series(Video):
    def __init__(self, title, year, genre, episode_number, season_number, play_count):
        super().__init__(title, year, genre, play_count)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        season_str = str(self.season_number).zfill(2)
        episode_str = str(self.episode_number).zfill(2)
        return f"{self.title} S{season_str}E{episode_str}"


media_list = []

media_list.append(Movie("Pulp Fiction", 1994, "Crime", 0))
media_list.append(Movie("The Shawshank Redemption", 1994, "Drama", 0))
media_list.append(Movie("Inception", 2010, "Action", 0))
media_list.append(Movie("The Godfather", 1972, "Crime", 0))
media_list.append(Movie("Fight Club", 1999, "Drama", 0))

media_list.append(Series("The Simpsons", 1989, "Animation", 5, 1, 0))
media_list.append(Series("Friends", 1994, "Comedy", 10, 236, 0))
media_list.append(Series("Breaking Bad", 2008, "Crime", 5, 62, 0))
media_list.append(Series("Game of Thrones", 2011, "Fantasy", 8, 73, 0))
media_list.append(Series("Stranger Things", 2016, "Drama", 4, 34, 0))
movies = []
series = []

print("Zawartość:")
for video in media_list:
    print(video)


def get_movies():
    for video in media_list:
        if isinstance(video, Movie):
            movies.append(video)
    movies.sort(key=lambda movie: movie.title)
    return movies


def get_series():
    for video in media_list:
        if isinstance(video, Series):
            series.append(video)
    series.sort(key=lambda series: series.title)
    return series


get_movies()
get_series()

print("Filmy:")
for movie in movies:
    print(movie)

print("\nSeriale:")
for series in series:
    print(series)


# Search function using regex
def search_regex_in_objects(regex_pattern, object_list):
    result = []
    for obj in object_list:
        if re.search(regex_pattern, obj.title, re.IGNORECASE | re.MULTILINE):
            result.append(obj)
    return result


if __name__ == "__main__":
    text = input("Jakiego filmu szukasz? ")

    search_results = search_regex_in_objects(text, media_list)

    # Print search results
    for obj in search_results:
        print(obj.title)


def generate_views():
    video = random.choice(media_list)
    views = random.randint(1, 100)
    video.play_count = + views
    print(f"Dodano {views} odtworzeń dla: {video.title}")


def run_generate_views():
    for _ in range(10):
        generate_views()


run_generate_views()


def top_titles(media_list, count):
    sorted_media = sorted(media_list, key=lambda video: video.play_count, reverse=True)
    top_titles = [video.title for video in sorted_media[:count]]
    return top_titles


popular_titles = top_titles(media_list, 3)
print("Najpopularniejsze tytuły:")
for title in popular_titles:
    print(title)
