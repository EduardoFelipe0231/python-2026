#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

import time

print('=========== LOJAS 100 ===========')
valor = float(input('Qual o valor das compras? R$ '))
print("""
☞ [ 1 ] - à vista dinheiro/cheque: 10% de desconto
☞ [ 2 ] - à vista no cartão: 5% de desconto
☞ [ 3 ] - em até 2x no cartão: preço formal 
☞ [ 4 ] - 3x ou mais no cartão: 20% de juros
""")
time.sleep(1)
forma = int(input('Qual a forma de pagamento? '))

# so vai aparecer se a opção == 4
if forma == 4:
    parcelas = int(input('Digite o parcelamento: '))
    parcelamento3x = (valor +  valor * 20 / 100 ) / parcelas


vista = valor - ( valor * 10 / 100)
vista_cartao = valor - ( valor * 5 / 100)
parcelamento2x = valor / 2


if forma == 1:
    print('Forma de pagamento 1')
    print(f'O valor de R$ {valor:.2f} 🏷 - será de: R$ {vista:.2f} com 10% de desconto. ')
elif forma == 2:
    print('Forma de pagamento 2')
    print(f'O valor R$ {valor:.2f} - será de: R$ {vista_cartao:.2f} com 5% de desconto no cartão.')
elif forma == 3:
        print('Forma de pagamento 3')
        print(f'O valor R$ {valor:.2f} - será de: R$ {parcelamento2x:.2f} por mês em 2x sem juros.')
elif forma == 4:
    if forma == 4 and parcelas >= 3:
        print('Forma de pagamento 4')
        print(f'O valor R$ {valor:.2f} - será de: R$ {parcelamento3x:.2f} por mês - com 20% juros - em {parcelas}x vezes.' )
    else:
        print('Somente para parcelar igual ou acima de 3x')
else:
    print('❌ Pagamento não encontrado...')