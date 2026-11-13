#Um programador que se preze necessita dominar vários tipos de estruturas de
#dados. Uma das estruturas mais importantes, em programas, são as matrizes.
#Assim, construa um programa que recebe duas matrizes inteiras de ordem 5 e
#imprima a soma e a diferença entre as matrizes.

matriz_1 = []
matriz_2 = []
matriz_soma = []
matriz_subtracao = []

print ("Digite os numeros da Matriz 1")
for i in range (2):
    linha_1 = []
    for j in range(2):
        print (f"Digite o numero da linha {i} coluna {j} ")
        linha_1.append(int(input()))
    matriz_1.append (linha_1)

print ("Digite os numeros da Matriz 2")
for i in range (2):
    linha_2 = []
    for j in range(2):
        print (f"Digite o numero da linha {i} coluna {j} ")
        linha_2.append(int(input()))
    matriz_2.append (linha_2)

for i in range (2):
    linha_soma = []
    for j in range (2):
        linha_soma.append (matriz_1[i][j] + matriz_2[i][j])
    matriz_soma.append(linha_soma)

for i in range (2):
    linha_subtracao = []
    for j in range (2):
        linha_subtracao.append (matriz_1[i][j] - matriz_2[i][j])
    matriz_subtracao.append(linha_subtracao)

for i in range(matriz_soma):
    print (i)
for i in matriz_subtracao:
    print (i)