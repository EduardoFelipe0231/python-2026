#70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#1) qual é o total gasto na compra.

#2) quantos produtos custam mais de R$1000.

#3) qual é o nome do produto mais barato.

print('*'*40)
print('SUPER LOJA CPL')
print('*'*40)

total = 0
maior = 0

while True:
    product = str(input('Qual o produto ?  ' )).strip().lower()    
    price = float(input('🏷️ Quanto custou? R$ '))
    choice = ' '
    while choice not in 'sn':
        choice = str(input('Inserir outro produto [S/N]?  ')).strip().lower()

    #total compra total = total + price
    total += price

    #produtos mais que 1000 reais.
    if price >= 1000:
        maior+=1

    print('='*40)
    if choice == 'n':
        break

print(f'O total da compra foi de R$ {total:.2f}.')
print(f'Temos {maior} produtos maiores ou igual a R$ 1000')
    