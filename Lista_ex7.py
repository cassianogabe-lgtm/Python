# Construa um programa que leia informações (matrícula, nome, setor e salário) de 20 funcionários. Deve ser permitido executar quantas 
# consultas o operador desejar, em que ele digita a matrícula e são apresentados o setor e o salário. 
# Se a matrícula digitadanão existir, informar o usuário

matricula = []
nome = []
setor = []
salario = []


for i in range (2):

    matricula.append(int(input("Digite sua matrícula")))
    nome.append(input ("Digite seu nome"))
    setor.append(input ("Digite seu setor"))
    salario.append(float(input("Digite seu salário")))



while True:
    busca = int(input("Digite a matrícula que deseja consultar (ou 0 para sair): "))
    if busca == 0:
        break
    if busca in matricula:
        posicao = matricula.index(busca)
        print(setor[posicao])
        print(salario[posicao])
    
    else:
        print ("Matricula não encontrada")




