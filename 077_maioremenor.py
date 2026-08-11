#078: 
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
import time

print('/'*30)
print(f'{"Analisador de dados":^30}')
print('/'*30)

numeros = []
cont = 0


#lê 5 vezes o input e armazena na lista numeros.
while cont < 5:
    valor = int(input(f'Informe o valor {cont+1}°: '))
    numeros.append(valor)
    cont +=1

print('Validando...')
time.sleep(1)
print('Resultados 📊👇')
#mostra os valores
print(f'➜ Foram cadastrados {cont} valores: {numeros}', sep='')

#valida o maior e sua posição.
# é usado o enumerate para somar cada vez que o número aparece.
print(f'O maior valor foi o {max(numeros)} na posição: ', end='')
for p, i in enumerate(numeros):
    if max(numeros) == i:
        print(f'{p+1}°', end=', ')

#valida o menor e sua posição.     
print(f'\n O menor valor foi o {min(numeros)} na posição: ', end='')
for p, i in enumerate(numeros):
    if min(numeros) == i:
        print(f'{p+1}°', end=', ')


