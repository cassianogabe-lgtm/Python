#Construa um programa que efetue a leitura das quatro notas de 20 alunos, calcule e mostre a média de cada aluno e a média da turma.

media_aluno = 0
media_total = 0
soma_notas = 0
for i in range (20):
    soma_notas = 0
    for j in range (4):
        nota = float(input(f"Digite a{j+1}ª nota"))
        soma_notas = soma_notas + nota
    media_aluno = soma_notas / 4
    media_total = media_total + soma_notas
    print (f"A media do {i+1} aluno é {media_aluno:.2f}")
print (f"A media da turma é: {media_total / 80:.2f}")

        

