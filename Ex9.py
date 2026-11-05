salario = float(input("Digite seu salário"))
print ("Escolha o cargo desejado digitando o número do mesmo")
print ("1 - Servente")
print ("2 - Pedreiro")
print ("3 - Mestre de obras")
print ("4 - Tecnico de segurança")
cargo = int(input())
if cargo == 1:
    aumento = salario * 0.4
    print ("Cargo: Servente, Valor do aumento:",aumento, "Novo salário:", salario + aumento)
elif cargo == 2:
    aumento = salario * 0.35
    print ("Cargo: Pedreiro, Valor do aumento:",aumento, "Novo salário:", salario + aumento)
elif cargo == 3:
    aumento = salario * 0.2
    print ("Cargo: Mestre de obras, Valor do aumento:",aumento, "Novo salário:", salario + aumento)
elif cargo == 4:
    aumento = salario * 0.1
    print ("Cargo: Tecnico de segurança, Valor do aumento:",aumento, "Novo salário:", salario + aumento)
else:
    print("Número de vargo inválido")