print ("Escolhe um prato conforme as opções abaixo:")
print ("Opção 1 - Prato Italiano")
print ("Opção 2 - Prato Japônes")
print ("Opção 3 - Prato Salvadorenho")
prato = int(input())
if prato ==1:
    prato = 750
elif prato ==2:
    prato =324
elif prato==3:
    prato =545
else:
    prato = 0
    print("prato inválido")
print ("Escolhe uma bebida conforme as opções abaixo:")
print ("Opção 1 - Chá")
print ("Opção 2 - Suco de laranja")
print ("Opção 3 - Refrigerante")
bebida = int(input())
if bebida ==1:
    bebida =30
elif bebida == 2:
    bebida = 80
elif bebida == 3:
    bebida = 90
else:
    bebida = 0
    print ("Bebida inválida")
calorias = prato + bebida
print("O total de calorias do seu prato + bebida escolhidos é:", calorias)
