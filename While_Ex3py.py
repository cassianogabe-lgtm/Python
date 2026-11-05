numero = int(input("Digite um numero inteiro:"))
divisor = 2
divisores_encontrados  = 0
while divisor < numero:
     resto = numero % divisor
     if resto == 0: 
        divisores_encontrados = divisores_encontrados + 1
     divisor = divisor + 1
if divisores_encontrados == 0:
    print ("Não é primo")
else:
    print ("É primo")
     
         