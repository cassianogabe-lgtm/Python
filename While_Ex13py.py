while True:
    numero_pedido = int(input("Digite o número do pedido (0 para sair): "))
    
    if numero_pedido == 0:
        break  # <--- BATEU O 0 AQUI? O programa pula fora do loop NA HORA!
        
    # Se não foi 0, o programa continua daqui para baixo normalmente:
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))
    preco = float(input("Digite o preço unitário: "))
    quantidade = int(input("Digite a quantidade: "))
    
    subtotal = preco * quantidade
    total_geral = total_geral + subtotal