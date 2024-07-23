import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e35214f728f9cb8d3a2d000f30c66e8d'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}

body_putname = {
    "pokemon_id": "44753",
    "name": "Pupok",
    "photo_id": 705
}

body_pokeball = {
    "pokemon_id": "44753"
}


'''Создаем покемона'''
'''response_create = requests.post(url=f'{URL}/pokemons',headers=HEADER, json=body_create)
print(response_create.text)'''

'''Меняем покемону имя'''
'''response_putname = requests.put(url= f'{URL}/pokemons', headers=HEADER, json=body_putname)
print(response_putname.text)
'''

'''Ловим покемона в покеболл'''
response_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball',headers=HEADER, json=body_pokeball)
print(response_pokeball.text)

