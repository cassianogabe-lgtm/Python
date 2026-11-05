idade = int(input("Digite sua idade"))
print ("Qual sua opinião?")
print (" 1- Satisfatório")
print (" 2- Indiferente")
print (" 3- Insatisfatório")
opiniao = int(input())
satisfatorio = 0
insatisfatorio = 0
soma_idade = 0
while idade !=0:
    if opiniao == 1:
        satisfatorio = satisfatorio + 1
        soma_idade = soma_idade + idade
    if opiniao == 3:
        insatisfatorio = insatisfatorio + 1
    idade = int(input("Digite sua idade"))
    print ("Qual sua opinião?")
    print (" 1- Satisfatório")
    print (" 2- Indiferente")
    print (" 3- Insatisfatório")
    opiniao = int(input())
print ("Numero de clientes que responderam satisfatório =", satisfatorio)
if satisfatorio !=0:
    print ("Media de idade dos clientes que responderam satisfatório", soma_idade / satisfatorio)
else:
    print ("Nenhum cliente escolheu a opção satisfatório, por isso não foi calculado a media de idade")
print ("Numero de clientes que responderam insatisfatório =", insatisfatorio)


   
