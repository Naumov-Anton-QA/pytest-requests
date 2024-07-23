import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e35214f728f9cb8d3a2d000f30c66e8d'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_LEVEL = '1'
TRAINER_ID = '6383'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers',params={'level': '1'})
    assert response.status_code ==200

def test_status_code():
    response = requests.get(url=f'{URL}/trainers',params={'trainer_id': TRAINER_ID})
    assert response.status_code ==200

