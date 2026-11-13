#É possível criar sistemas para organização e controle de estoque nas mais diversas
#áreas. Assim sendo, elabore um programa para efetuar o cadastro de 20 livros
#e imprimi-los. O cadastro deve conter as seguintes informações: título, autor, editora, edição e ano.

lista_livros = []

for i in range (2):
    dados = {
        'titulo':"",
        'autor':"",
        'editora':"",
        'edição': 0,
        'ano': 0,
    }


    print (f"Escreva o titulo do {i+1} livro")
    dados['titulo'] = input()
    print (f"Escreva o autor do {i+1} livro")
    dados['autor'] = input()
    print (f"Escreva a editora do {i+1} livro")
    dados['editora'] = input()
    print (f"Escreva a edição do {i+1} livro")
    dados['edição'] = int(input())
    print (f"Escreva o ano do {i+1} livro")
    dados['ano'] = int(input())
    lista_livros.append(dados)
contador = 1
for dados in lista_livros:
    print(f"============ LIVRO{contador}============")
    print("Titulo:",dados['titulo'])
    print("Autor:",dados['autor'])
    print("Editora:",dados['editora'])
    print("Edição:",dados['edição'])
    print("Ano:",dados['ano'])
    print()
    contador = contador + 1


