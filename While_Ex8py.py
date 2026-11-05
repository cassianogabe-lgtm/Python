n = int(input("Digite o valor de N"))
s = 0
soma = 0
for cont in range (1,n + 1,1):
    s = 1 / cont
    soma = soma + s
print("Resultado =",soma)