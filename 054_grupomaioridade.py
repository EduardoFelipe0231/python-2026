#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime as dt
import time

print('*'*40)
print('\033[95m Verificador de idades')
print('\033[m*'*40)

#contadores que são usados dentro do for e if - eles ajudam a pegar o valor de quantos foi verdadeiro para aquela açaõ.
#soma_pessoas = 1
count_maior = 0
count_menor = 0
idade = dt.datetime.today().year - 18 #2008

#for.
for i in range (7):
    p = int(input(f'Digite o {i+1}° ano de nascimento:  '))
    #p = int(input(f'Digite o {i+1}° ano de nascimento:  '))
    #soma_pessoas += 1 #a cada laço no input ele soma + 1 e adiciona acima no input.
    if p <= idade:
        count_maior += 1
    else:
        count_menor += 1

print('Calculando...')
time.sleep(2)

print(f'Nos temos {count_maior} pessoas maiores de idade \n E também temos {count_menor} menores de idade')
