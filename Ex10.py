estado = int(input("Digite o número do estado (1 ao 4)"))
peso = float(input("Digite o peso da carga (toneladas)"))
codigo = int(input("Digite o código da carga (entre 10 e 40)"))
if codigo >=10 and codigo <=20:
    preco = peso*1000*180
    print ("Peso:", peso, "Preço:", preco)
elif codigo <=30:
    preco = peso*1000*120
    print ("Peso:", peso, "Preço:", preco)
else:
    preco = peso*1000*230
    print ("Peso:", peso, "Preço:", preco)
if estado == 1:
    imposto = preco * 0.2
    print ("Imposto:",imposto, "Valor total:", preco + imposto)
elif estado == 2:
    imposto = preco * 0.15
    print ("Imposto:",imposto, "Valor total:", preco + imposto)
elif estado == 3:
    imposto = preco * 0.10
    print ("Imposto:",imposto, "Valor total:", preco + imposto)  
elif estado == 4:
    imposto = preco * 0.05
    print ("Imposto:",imposto, "Valor total:", preco + imposto)    