altura = float(input("Digite sua altura"))
sexo = input("Digite seu sexo, M ou F?")
if sexo == "M" or "m":
    print("Seu peso ideal é = ", 72.7 * altura - 58)
elif sexo == "F" or "f":
    print ("Seu peso ideal é =", 62.1 * altura - 44.7)
else:
    print ("Sexo inválido")
