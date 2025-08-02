from searches import fetch_universities_by_name, fetch_universities_by_country, fetch_universities_in_Brazil

while True:
    option = input('''
1 - Buscar universidades pelo nome
2 - Buscar universidades por país
3 - Buscar universidades do Brasil
4 - Sair
Selecione a opção desejada:''')

    if option == '1':
        fetch_universities_by_name()

    elif option == '2':
        fetch_universities_by_country()

    elif option == '3':
        fetch_universities_in_Brazil()
        
    elif option == '4':
        print('bye bye...saindo...')
        break
    else:
        print('\nDigite uma opção válida\n')
        pass