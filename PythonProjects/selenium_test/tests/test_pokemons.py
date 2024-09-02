import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'bc8c989e8781cf4787d0e78b86c57591'
HEADER = {'Content-Type': 'application/json','trainer_token':TOKEN}
trainer_id = '5271'
def test_status_code():
    response =requests.get(url=f'{URL}/trainers',params= {'trainer_id':trainer_id})
    assert response.status_code == 200
  
def test_part_of_response():
    response =requests.get(url=f'{URL}/trainers',params= {'trainer_id':trainer_id})
    assert response.json()["data"][0]["trainer_name"] == 'Никита'
    




    