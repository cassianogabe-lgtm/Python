#A computação, frequentemente, é utilizada para servir de ferramenta na identificação
#de diferenças ou semelhanças entre objetos. Dessa forma, faça um programa que leia
#duas listas A e B, cada uma com 5 elementos. Para cada elemento presente na lista A,
#mostre quantos elementos iguais ao respectivo elemento existem na lista B.

lista_A = []
lista_B = []
for i in range (5):
    print (f"Digite o {i+1} elemento da lista A")
    lista_A.append(int(input()))

for i in range (5):
    print (f"Digite o {i+1} elemento da lista B")
    lista_B.append(int(input()))

for elemento_A in lista_A:
    contador = 0
    for elemento_B in lista_B:
        if elemento_A == elemento_B:
            contador = contador + 1
    print (f"quantidade = {contador}")
    print (f"elemento = {elemento_A}")

