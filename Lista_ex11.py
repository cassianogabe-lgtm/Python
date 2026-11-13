#Um dos principais benefícios de aprender a programar é o fato de que é possível
#automatizar tarefas repetitivas. Dessa forma, faça um programa que leia uma
#palavra e o número de vezes que se deseja imprimi-la. Em seguida, realize as
#impressões da respectiva palavra, de acordo com o desejo do usuário.

palavra = input("Digite uma palavra")
numero_vezes = int(input("Digite o número de vezes que deseja imprimir a palavra"))

for i in range (numero_vezes):
    print (palavra)
