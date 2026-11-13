#É comum, em uma aplicação, ter de determinar quais números são pares ou ímpares dentre todos os valores de um conjunto de dados. 
#Dessa forma, faça um programa que verifique se determinado número é positivo ou negativo, por meio de uma função.


def verificar_numero(numero):
    if numero > 0:  
        return("Número positivo")
    elif numero < 0:
        return ("Número negativo")
    else:
      return ("Zero não é positivo nem negativo")

numero1 = int(input("Digite um número para verificar se o mesmo é positivo ou negativo"))
resultado = verificar_numero(numero1)
print (resultado)
