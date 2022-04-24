import requests


def get_pokemon_info(name):

    print("Getting Pokemon info...", end=''),
    

    url = "https://pokeapi.co/api/v2/pokemon/" + name 
    resp_msg = requests.get(url)
    
    if resp_msg.status_code == 200:
        print('success')
        return resp_msg.json() 
    else:
        print('failed. Code:', resp_msg.status_code), 
        return

def get_pokemon_img_url(name):

    pokemon_dict = get_pokemon_info(name)

    if pokemon_dict:
        print(pokemon_dict)
        return pokemon_dict['sprites']['other']['official-artwork']['front_default']
        
    else:
        print("failed image")

def get_poke_list(limit=100, offset=0):
    url ='https://pokeapi.co/api/v2/pokemon/'

    params = {
        'limit':limit,
        'offset': offset
    }

    resp_img = requests.get(url, params=params)

     
    if resp_img.status_code == 200:
        
        dict = resp_img.json()

        return [p['name'] for p in dict['results']]
    else:
        print('Failed to get pokemon list.')
        print('Response code:',resp_img.status_code)
        print(resp_img.text) 
        return
