#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

lista_numeros = []
total = 0
cont = 0

for num in range(0, 6):
    inteiro = int(input('Digite o valor: '))
    print('--')
    lista_numeros.append(inteiro)

for soma in lista_numeros:
    if soma % 2 == 0:
        total += soma
        cont += 1

print(f'Entre os {cont} valores pares informados, a soma total dos valores são de: {total}')
