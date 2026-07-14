produto_valor = float(input("Qual o preço do produto? R$ "))
desconto_valor = int(input('Digite o valor para o desconto: '))

desconto = produto_valor - (produto_valor * desconto_valor / 100 )

print(f'O valor de R$ {produto_valor:.2f} com {desconto_valor} % de desconto, você vai pagar R$ {desconto:.2f}')

