numero = int(input("Digite um numero"))
soma_numeros = 0
quantidade_numeros = 0
menor_numero = 999999999999999999999999999999999999999999999999999999
maior_numero = 0
par_numero = 0
impar_numero = 0
while numero != 0:
    resto = numero % 2
    if resto == 0:
        par_numero = par_numero + 1
    else:
        impar_numero = impar_numero + 1
    if maior_numero < numero:
        maior_numero = numero
    if menor_numero > numero:
        menor_numero = numero
    soma_numeros = soma_numeros + numero
    quantidade_numeros = quantidade_numeros + 1
    numero = int(input("Digite um numero"))
print ("A média dos valores é:", soma_numeros / quantidade_numeros)
print ("O maior número digitado foi:", maior_numero)
print ("O menor número digitado foi:", menor_numero)
print ("A quantidade de números impares digitados foi:", impar_numero)
print ("A quantidade de números pares digitados foi:", par_numero)