from searches import (
    fetch_universities_by_name,
    fetch_universities_by_country,
    fetch_universities_in_Brazil,
    adicionar_favorito,
    listar_favoritos,
    deletar_favorito,
    editar_favorito
)

while True:
    option = input('''
========== UniSearch ==========
1 - Buscar universidades pelo nome
2 - Buscar universidades por país
3 - Buscar universidades do Brasil
4 - Adicionar universidade favorita
5 - Listar universidades favoritas
6 - Deletar universidade favorita
7 - Editar universidade favorita
8 - Sair
Selecione a opção desejada: ''')

    if option == '1':
        fetch_universities_by_name()
    elif option == '2':
        fetch_universities_by_country()
    elif option == '3':
        fetch_universities_in_Brazil()
    elif option == '4':
        adicionar_favorito()
    elif option == '5':
        listar_favoritos()
    elif option == '6':
        deletar_favorito()
    elif option == '7':
        editar_favorito()
    elif option == '8':
        print('bye bye...saindo...')
        break
    else:
        print('\nDigite uma opção válida\n')
        pass