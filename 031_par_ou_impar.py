#Crie um programa que leia um número inteiro e mostre se é par ou ímpar.

num = int(input("Digite o valor:"))

if num % 2 == 0:
    print(f"O número {num}, é par")
else:
    print(f"O número {num}, é ímpar")