numero1 = int(input("Digite o primeiro numero"))
numero2 = int(input("Digite o segundo numero"))
numero3 = int(input("Digite o terceiro numero"))
numero4 = int(input("Digite o quarto numero"))
numero5 = int(input("Digite o quinto numero"))
maior = numero1
menor = numero1
if numero1 < numero2:
    maior = numero2
if numero1 > numero2:
    menor = numero2
if numero3 > maior:
    maior = numero3
if numero3 < menor:
    menor = numero3
if numero4 > maior:
    maior = numero4
if numero4 < menor:
    menor = numero4
if numero5 > maior:
    maior = numero5
if numero5 < menor:
    menor = numero5
print ("O maior número digitado é", maior)
print ("O menor número digitado é", menor)
