#O processamento de dados textuais, atualmente, é bastante avançado, e já existem bibliotecas capazes de auxiliar neste tipo de situação. 
#Elabore um programa que leia uma palavra e, se ela tiver número ímpar de caracteres, imprima todasas suas vogais

palavra = input("Digite uma palavra")
minusculo = palavra.lower()
caracteres = len(minusculo)

resto = caracteres % 2
if resto == 0:
    print ("A palavra possui número par de caracteres")
else:
    print ("A palavra possui número impar de caracteres")
    for i in minusculo:
        if i in "aeiou":
            print(i)
    print (f"Essas são as vogais de {palavra}")
        
        
    
