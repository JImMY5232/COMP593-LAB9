import requests


def get_pokemon_info(url):
    print("Getting Pokemon info...", end=''),
    

    ulrl = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY" + url
    resp_msg = requests.get(ulrl)
