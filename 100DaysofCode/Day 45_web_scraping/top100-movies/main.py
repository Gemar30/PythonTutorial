import json
import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"

soup = BeautifulSoup(requests.get(url).content, "html.parser")
data = json.loads(soup.select_one("#__NEXT_DATA__").contents[0])

#print(json.dumps(data, indent=4))


def find_articles(data):
    if isinstance(data, dict):
        for k, v in data.items():
            if k.startswith("ImageMeta:"):
                yield v["titleText"]
            else:
                yield from find_articles(v)
    elif isinstance(data, list):
        for i in data:
            yield from find_articles(i)

movies = find_articles(data)


with open("movie.txt", mode = "w") as file:
    for a in movies:
        file.write(f"{a}\n")


