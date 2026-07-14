# Ler um valor do produto e cancular valor a vista PIX e valor normal sem desconto.

produto = float(input("Digite o valor - R$ "))

pix = produto - (produto * 5 / 100)
parcelado =  produto + (produto * 15 / 100 )


print(f'O produto custa R$ {produto:.2f} \n 🏷️ Valores: \n ↘️  A vista R$ {pix:.2f} \n ↘️  Parcelado R$ {parcelado:.2f}')