import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e4e2ebc9fb19e38436f1ba1c804cc401'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print (response_create.text)'''

body_change = {
    "pokemon_id": "297089",
    "name": "Кукусик",
    "photo_id": 2
}

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print (response_change.text)'''

body_add = {
    "pokemon_id": "297089"
}

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print (response_add.text)
