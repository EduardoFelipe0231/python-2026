#074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random

tupla = (random.randint(0,10), (random.randint(0,10)), (random.randint(0,10)), (random.randint(0,10)))

print(f'Os números sorteados foram: ', end='')
for i in tupla:
    print(f' {i} ', end=' ')

print(f'\n O maior valor foi {max(tupla)}')
print(f' O menor valor foi {min(tupla)}')