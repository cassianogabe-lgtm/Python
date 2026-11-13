#faça um programa que efetue a leitura dos nomes de cinco alunos e, também, de suas quatro notas
#bimestrais. Calcule a média de cada aluno e apresente os nomes classificados em ordem crescente de média.
media = 0
media_lista = []
aluno_lista =[]
for i in range(5):
    soma_nota = 0
    aluno = input("Digite o nome do aluno")
    aluno_lista.append(aluno)
    for j in range (4):
        nota = int(input(f"Digite a {j+1} nota"))
        soma_nota = soma_nota + nota
    media = soma_nota / 4
    media_lista.append(media)

for cont in range(4):
    for j in range(4):
        if media_lista[j] > media_lista[j+1]:
            temporaria = media_lista[j]
            media_lista[j] = media_lista[j+1]
            media_lista[j+1] = temporaria
            temporaria = aluno_lista[j]
            aluno_lista[j] = aluno_lista[j+1]
            aluno_lista[j+1] = temporaria
for i in range(5):
    print(aluno_lista[i], media_lista[i])