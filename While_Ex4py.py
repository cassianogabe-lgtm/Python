salario = float(input("Qual seu salário")) 
filhos = int (input("Quantos filhos você tem"))
soma_salario = 0
soma_filhos = 0
pessoas = 0
maior_salario = 0

while salario != -1:
    soma_salario = soma_salario + salario
    soma_filhos = soma_filhos + filhos
    pessoas = pessoas + 1
    if maior_salario < salario:
        maior_salario = salario
    salario = float(input("Qual seu salário")) 
    if salario !=-1:
        filhos = int (input("Quantos filhos você tem"))
media_salario = soma_salario / pessoas
media_filhos = soma_filhos/ pessoas
print ("Media de salario =", media_salario)
print ("Media de filhos =", media_filhos)
print ("Maior salario é:", maior_salario)
