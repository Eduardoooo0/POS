import requests
import json

url = 'http://127.0.0.1:8000/universidades'
url_fav = 'http://127.0.0.1:8000/favoritos'

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



def adicionar_favorito():
    print("Insira os dados da universidade:")
    name = input("Nome: ")
    country = input("País: ")
    domains = input("Domínio (ex: ufrn.br): ")
    web_pages = input("Página (ex: http://www.ufrn.br): ")

    dados = {
        "name": name,
        "country": country,
        "domains": domains,
        "web_pages": web_pages
    }

    r = requests.post(url_fav, json=dados)
    if r.status_code == 201:
        print("Universidade favorita adicionada com sucesso!")
    else:
        print(f"Erro: {r.status_code}")
        print(r.text)

def listar_favoritos():
    r = requests.get(url_fav)
    if r.status_code == 200:
        favoritos = json.loads(r.text)
        if favoritos:
            for i, f in enumerate(favoritos, start=1):
                print(f"\nID: {f['id']} | {f['name']} | {f['country']} | {f['domains']} | {f['web_pages']}")
        else:
            print("Nenhuma universidade favorita cadastrada.")
    else:
        print(f"Erro: {r.status_code}")
        print(r.text)

def deletar_favorito():
    id = input("Digite o ID da universidade que deseja deletar: ")
    r = requests.delete(f"{url_fav}/{id}")
    if r.status_code == 204:
        print("Favorito deletado com sucesso.")
    elif r.status_code == 404:
        print("Favorito não encontrado.")
    else:
        print("Erro ao deletar favorito.")
        print(r.text)

def editar_favorito():
    id = input("Digite o ID da universidade que deseja editar: ")

    print("Insira os novos dados:")
    name = input("Nome: ")
    country = input("País: ")
    domains = input("Domínio (ex: ufrn.br): ")
    web_pages = input("Página (ex: http://www.ufrn.br): ")

    dados = {
        "name": name,
        "country": country,
        "domains": domains,
        "web_pages": web_pages
    }

    r = requests.put(f"{url_fav}/{id}", json=dados)
    if r.status_code == 200:
        print("Favorito atualizado com sucesso!")
    elif r.status_code == 404:
        print("Favorito não encontrado.")
    else:
        print("Erro ao atualizar favorito.")
        print(r.text)