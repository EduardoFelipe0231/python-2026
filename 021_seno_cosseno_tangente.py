#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

ang = float(input("Digite um ângulo que deseja verificar: "))

seno = sin(radians(ang))
tang = tan(radians(ang))
coss = cos(radians(ang))

print(f'O valor do ângulo 📐 {ang:.0f}ºC  é de: \n ▸ SENO {seno:.2f} \n ▸ COSSENO {coss:.2f} \n ▸ TANGENTE {tang:.2f}')