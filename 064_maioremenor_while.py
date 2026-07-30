# 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
import time

continuar = 'S'
contador = 0
lista = []

while continuar == 'S':
    num = int(input('valor: '))
    continuar = str(input('Deseja continuar? [s/n]')).strip().upper()
    contador += 1
    lista.append(num)

#media
media = (sum(lista) / len(lista))
#maior
maior = max(lista)

print('Calculando..')
time.sleep(1)
print(f'Confira os valores digitados 👇✍🏻 \n Ao total fora {contador} números. \n ⇢ Temos de média {media} \n ⇢ O maior número é o {maior}')