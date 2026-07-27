#55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

peso_array = []
qtd = int(input('Quantos valores você quer digitar? '))

for p in range (qtd):
    valor = float(input(f'Qual o peso da {p+1}ª pessoa? (kg)  '))
    peso_array.append(valor) #adiciona os valores do input valor na lista.

print(f'Entre os {qtd} pesos informados, essa foi o resultado: \n O maior peso foi de: {max(peso_array)} Kg \n O menor peso foi de: {min(peso_array)} Kg')


