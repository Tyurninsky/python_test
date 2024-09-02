import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'bc8c989e8781cf4787d0e78b86c57591'
HEADER = {'Content-Type': 'application/json','trainer_token':TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_rename = {
    "pokemon_id": "66512",
    "name": "Бульбашзавр",
    "photo_id": 2
}
body_pokemons = {
    "pokemon_id": "66512"
}

'''requests_create = requests.post(url=f'{URL}/pokemons',headers=HEADER,json=body_create)
print(requests_create.text)  '''   

'''requests_rename = requests.put(url=f'{URL}/pokemons',headers=HEADER,json=body_rename)
print(requests_rename.text)'''

requests_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball',headers=HEADER,json=body_pokemons)
print(requests_pokeball.text)