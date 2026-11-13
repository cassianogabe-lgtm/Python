idade = int(input("Informe sua idade"))
nome = input("Informe seu nome")
if idade<=18:
    print ("Nome:",nome,"Idade:",idade,"mensalidade do plano de saúde = 50,00")
elif idade >18 and idade<30:
    print ("Nome:",nome,"Idade:",idade,"mensalidade do plano de saúde = 70,00")
elif idade >29 and idade<46:
    print ("Nome:",nome,"Idade:",idade,"mensalidade do plano de saúde = 90,00")
elif idade >45 and idade<66:
    print ("Nome:",nome,"Idade:",idade,"mensalidade do plano de saúde = 130,00")
else:
    print ("Nome:",nome,"Idade:",idade,"mensalidade do plano de saúde = 170,00")   