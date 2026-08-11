#079: 
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
from time import sleep

print('/'*30)
print(f'{"Validar de números adicionados":^30}')
print('/'*30)

numeros = []

while True:
    valor = int(input('Valor: '))   

    # se o "valor" digitado "não estiver" em "numeros", faça:
    if valor not in numeros:
        if valor < 0:
            print('Somente valores positivos :)')
        else:
            numeros.append(valor)
            print(f'Valor {valor} adicionado! ')
    else:
        print('Valor já existe na sua lista, tente outro..')

    mais = ' '
    mais = str(input('Adicionar outros? [S/N] ')).strip().upper()
    if mais == 'N':
        print('Programa finalizado ✌︎︎')
        sleep(1)
        break


print(f'Os valores digitados foram: {numeros}')
sleep(1)
print(f'\n ➤ Ordem crescente: {sorted(numeros)}')
