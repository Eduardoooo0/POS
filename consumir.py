import requests
import json

url = 'http://127.0.0.1:8000/universidades'

while True:
    option = input('1 - Buscar universidades pelo nome\n2 - Buscar universidades por país\n3 - Buscar universidades do Brasil\nSelecione a opção desejada:')

    if option == '1':
        university_name = input('Digite o nome:')
        r = requests.get(url=f'{url}/nome', params={"name": university_name})
        if r:
            dados = json.loads(r.text)
            for index,dado in enumerate(dados, start=1):
                print(f'{index} - {dado['name']} | {dado['country']} | {dado['domains']} | {dado['web_pages']}')
        else:
            print('erro')
    elif option == '2':
        pass

    else:
        pass