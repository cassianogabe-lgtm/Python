idade = int(input("Qual sua idade? (Digite 0 para encerrar)"))
peso = int (input("Qual seu peso?"))
print("Qual seu sexo?")
print("1 - Masculino")
print("2 - Feminino")
sexo = int(input())
print ("Qual seu estado civíl?")
print ("1 - Solteiro")
print ("2 - Casado")
print ("3 - Separado")
print ("4 - Viúvo")
estado_civil = int(input())
solteiro = 0
casado = 0
separado = 0
viuvo = 0
soma_idade = 0
soma_peso = 0
quantidade = 0
while idade != 0:
    if estado_civil == 1:
        solteiro = solteiro + 1
    if estado_civil == 2:
        casado = casado + 1
    if estado_civil == 3:
        separado = separado + 1
    if estado_civil == 4:
        viuvo = viuvo + 1
    soma_idade = soma_idade + idade
    soma_peso = soma_peso + peso
    quantidade = quantidade + 1
    idade = int(input("Qual sua idade? (Digite 0 para encerrar)"))
    if idade != 0:
        peso = int (input("Qual seu peso?"))
        print("Qual seu sexo?")
        print("1 - Masculino")
        print("2 - Feminino")
        sexo = int(input())
        print ("Qual seu estado civíl?")
        print ("1 - Solteiro")
        print ("2 - Casado")
        print ("3 - Separado")
        print ("4 - Viúvo")
        estado_civil = int(input())
print ("Solteiros:", solteiro)
print ("Casados:", casado)
print ("Separados:", separado)
print ("Viúvos:", viuvo)
print ("Média de idade =", soma_idade / quantidade)
print ("Média de peso =", soma_peso / quantidade)

    
    

