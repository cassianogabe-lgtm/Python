#Com o surgimento dos smartphones, a funcionalidade de agenda eletrônica passou a fazer parte do cotidiano das pessoas, de modo geral. 
#Pensando em um protótipo de agenda, faça um programa para efetuar o cadastro de 30 contatos.
#O cadastro deve conter as seguintes informações: nome, telefone e e-mail. Apresente todos os cadastros.

lista_contatos = []

for i in range (2):
    dados = {
        'nome': "",
        'telefone':"",
        'e-mail':"",
     }
    print (f"Cadastre o nome do {i+1} contato")
    dados ['nome'] = input()
    print (f"Cadastre o telefone do {i+1} contato")
    dados ['telefone'] = (input())
    print (f"Cadastre o e-mail do {i+1} contato")
    dados ['e-mail'] = input()
    lista_contatos.append(dados)

contador = 1
for contatos in lista_contatos:
    print (f"======= CONTATO{contador} =======")
    print ("Nome:", contatos['nome'])
    print ("Telefone:", contatos['telefone'])
    print ("E-mail:", contatos['e-mail'])
    print()
    contador = contador + 1
# criado tambem opção de pesquisar pelo nome do contato
pesquisa = input("Digite o nome que deseja pesquisar")
for i in lista_contatos:
    if i['nome'] == pesquisa:
        print ("Nome:", i ['nome'])
        print ("Telefone:", i ['telefone'])
        print ("E-mail:", i ['e-mail'])
        break
else:
    print("Contato não encontrado")

