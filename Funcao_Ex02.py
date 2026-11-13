#Escreva um programa utilizando uma função que receba o peso de um peso em quilogramas e o converta para libras
def converter (kg):
    libras = kg * 2.20462
    return libras

peso = float(input("Digite o peso em kg"))
resultado = converter(peso)
print(f"O peso convertido em libras é: {resultado:.2f}")