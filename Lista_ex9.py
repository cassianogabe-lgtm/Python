lista = []
for i in range (5):
    print ("Digite os 5 números da lista, após a lista será exibida em ordem decrescente")
    lista.append(int(input(f"Digite o {i+1} da lista")))
lista.sort(reverse = True)
print(lista)