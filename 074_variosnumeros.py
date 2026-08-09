#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#Quantas vezes apareceu o valor 9.
#Em que posição foi digitado o primeiro valor 3.
#Quais foram os números pares.

print('-='*40)
print(' Análise de números')
print('-='*40)

numero = int(input('Qual o primeiro? '))
numero2 = int(input('Qual o segundo? '))
numero3 = int(input('Qual o terceiro? '))
numero4 = int(input('Qual o quarto? '))

total = (numero, numero2, numero3, numero4)

print('-'*30)

print('Os números pares são: ', end='')
for b in total:
    if b % 2 == 0:
        print(b, end=' ')