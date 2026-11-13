#Provavelmente, você já deve ter se deparado com uma situação na qual é preciso
#calcular o somatório de valores compreendidos dentro de um intervalo determinado.
#Por isso, elabore uma função que receba dois números positivos por parâmetro e
#retorne a soma dos N números inteiros existentes entre eles.

def somar_intervalo (numero1, numero2):
    soma = 0
    for i in range (numero1 + 1, numero2):
        soma = soma + i
    return soma

print ("Digite dois numeros e o programa irá retornar o resultado da soma dos numeros que ficam entre os que você digitou ")

primeiro_numero = int(input("Digite o primeiro número"))
segundo_numero = int(input("Digite o segundo número"))
if primeiro_numero > segundo_numero:
    temporaria = primeiro_numero
    primeiro_numero = segundo_numero
    segundo_numero = temporaria

resultado = somar_intervalo (primeiro_numero, segundo_numero)
print (resultado)



