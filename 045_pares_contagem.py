#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

num = int(input('Digite um número de 0 a 100:  '))

if num < 0 or num > 100:
    print('Ops, digite um valor entre 0 a 100')
else:
  for i in range(0, num+1, 2):
        print(f'{i}', end=',')
print('fim')

