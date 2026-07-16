#Import math          
#from math import ceil
#from math import ceil;floor


# math - ceil / floor / trunc / pow / sqrt / factorial

###
### criar um programa que leia um numero real pelo teclado e, mostre a sua porção inteira ex: 8.231 -> 8

import math

user = float(input('Digite um valor aqui:'))

## usando o trunc () ou o int() ele corta qualquer valor apos o ponto.
new = math.trunc(user)
#new = int(user)

print(f'O valor é {new}')