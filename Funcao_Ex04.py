 #Elabore uma função que receba uma string e retorne a quantidade de consoantes

def contar_consoantes (palavra):
    quantidade = 0
    for letra in palavra:
        if letra.isalpha() and letra not in "aeiouáàâãéêíóôõú":
            quantidade = quantidade + 1
    return quantidade

palavra_digitada = input("Digite uma palavra")
palavra_digitada = palavra_digitada.lower()
resultado = contar_consoantes(palavra_digitada)
print (resultado)