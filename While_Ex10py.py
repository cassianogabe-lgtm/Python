soma = 0
for cont in range (200, 500 + 1, 1):
    resto = cont % 2
    if resto == 0:
        soma = soma + 0
    else:
        soma = soma + cont
print (soma)  
