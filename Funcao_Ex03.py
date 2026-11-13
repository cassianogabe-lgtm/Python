# Faça uma função que receba, como parâmetro, uma lista com três números inteiros
#e retorne-os, ordenados, em forma crescente.#

def ordenar(numeros):
    crescente = sorted(numeros)
    return crescente
lista = []
for i in range (3):
    print(f"Digite o {i+1}  número inteiro") 
    lista.append(int(input()))
resultado = ordenar(lista)
print (resultado)
                                       

 
 
 
 
 
 
 
 