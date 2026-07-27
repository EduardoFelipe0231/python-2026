#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Número: '))
total = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        print(f'\033[32m{i}', end=' ')
        total += 1
    else:
        print(f'\033[31m{i}', end=' ')
print(f'\n\033[m O número {numero} foi divisível {total} vezes.')

if total != 2:
    print('Não é primo')
else:
    print('é primo!!')

