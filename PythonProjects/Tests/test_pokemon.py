import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e4e2ebc9fb19e38436f1ba1c804cc401'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

def test_stats_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_trainer():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : '30676'}) 
    assert response.json()['data'][0]['trainer_name'] == 'Амадей Орфей Вены'