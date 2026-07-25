#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from  time import sleep
import datetime as dt

print(f'{' CONTAGEM REGRESSIVA ':*^50}')

year = dt.datetime.today().year

time = 10

for i in range (time, 0, -1 ):
    print(f'{i}')
    sleep(1)

print(f'FELIZ {year}!! °🥂⋆.ೃ🍾࿔*:･')