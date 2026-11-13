#Escreva um programa utilizando uma função que converta dada temperatura lida
#de Celsius para Fahrenheit

def converter(celsius):
    fahrenheit = (9*celsius) / 5 + 32
    return fahrenheit

temperatura = float(input("Digite a temperatura em graus celsius"))
resultado = converter(temperatura)
print (resultado)