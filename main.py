def changename(name):
    #Procedimento para transformar caracteres em maiúscula
    nameupper = name.upper()
    print(nameupper)

    #Procedimento para transformar string em lista
    namelist = list(nameupper)

    #Estrutura de repetição para correr pelo array e fazer as substituições
    for i in range(0, len(namelist)):
        #Estrutura condicional para fazer a substituição dos caracteres
        if namelist[i] == 'A':
            namelist[i] = '@'
        elif namelist[i] == 'E':
            namelist[i] = '&'
        elif namelist[i] == 'I':
            namelist[i] = '!'
        elif namelist[i] == 'O':
            namelist[i] = '#'
        elif namelist[i] == 'U':
            namelist[i] = '*'

    #Procedimento para juntar lista em uma string
    changedname = ''.join(namelist)

    print(changedname)

#PROGRAMA PRINCIPAL

#Dados de entrada
name = input('Digite um nome: ')

#Função para substituir os caracteres usando o nome como parâmetro
changename(name)

