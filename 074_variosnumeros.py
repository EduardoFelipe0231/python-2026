#075: 
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
# No final, mostre:
#Quantas vezes apareceu o valor 9.
#Em que posição foi digitado o primeiro valor 3.
#Quais foram os números pares.

print('-='*40)
print(' Análise de números')
print('-='*40)

cont = 0

#tupla com vários itens para digitar.
num = (int(input('Digite um número:')), 
       int(input('Digite o segundo número:')),
       int(input('Digite o terceiro número:')),
       int(input('Digite o quarto número:')))

print('*'*30)

#lista os valores armazenados dentro da tupla
print(f'Os números digitados foram: {num}')
#conta quantas vezes o número 4 apareceu.
# usar o IF x in x para validar se algo existe na tupla ou na variável.
if 4 in num:
    print(f'O valor 4 apareceu {num.count(4)} vezes dessa vez')
else:
    print('O número 4 não foi digitado.')
#em qual posição o valor 1 apareceu.
if 1 in num:
    print(f'O número 1 apareceu {num.index(1)+1}ª na posição.')
else:
    print('O número 1 não foi digitado.')
# ver se temos par.
for i in num:
    if i % 2 == 0:
        print(f' {i} ', end=' ')
        cont += 1
print(f'Temos {cont} valores pares, são eles:')
