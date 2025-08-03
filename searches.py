import requests
import json

url = 'http://127.0.0.1:8000/universidades'


def fetch_universities_by_name():
    university_name = input('Digite o nome da universidade:')
    r = requests.get(url=f'{url}/nome', params={"name": university_name})
    if r:
        dados = json.loads(r.text)
        if len(dados) != 0:
            for index,dado in enumerate(dados, start=1):
                print(f'{index} - {dado['name']} | {dado['country']} | {dado['domains']} | {dado['web_pages']}')
                print('-'*170)
        else:
            print('\nNenhuma universidade com esse nome encontrada!\n')
    else:
        print('\nerror\n')

def fetch_universities_by_country():
    university_country = input('Digite o país:')
    r = requests.get(url=f'{url}/pais', params={"country": university_country})
    if r:
        dados = json.loads(r.text)
        if len(dados) != 0:
            for index,dado in enumerate(dados, start=1):
                print(f'{index} - {dado['name']} | {dado['country']} | {dado['domains']} | {dado['web_pages']}')
                print('-'*170)
        else:
            print('\nNenhuma universidade encontrada!\n')
    else:
        print('\nerror\n')

def fetch_universities_in_Brazil():
    r = requests.get(url=f'{url}/pais', params={"country": "Brazil"})
    if r:
        dados = json.loads(r.text)
        if len(dados) != 0:
            for index,dado in enumerate(dados, start=1):
                print(f'{index} - {dado['name']} | {dado['country']} | {dado['domains']} | {dado['web_pages']}')
                print('-'*170)
        else:
            print('\nNenhuma universidade encontrada!\n')
    else:
        print('\nerror\n')