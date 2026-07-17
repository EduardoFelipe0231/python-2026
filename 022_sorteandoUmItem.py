from random import choice

import pygame

msg = 'Digite 5 itens para ser sorteados!'
print(f"{msg:=^50}")

i1 = str(input("Digite o primeiro item:"))
i2 = str(input("Digite o segundo item:"))
i3 = str(input("Digite o terceiro item:"))
i4 = str(input("Digite o quarto item:"))
i5 = str(input("Digite o quinto item:"))

list = [i1, i2, i3 ,i4 ,i5]

choice = choice(list)

print(f'O item sorteado para o ganhador foi {choice}, parabéns!!! 🎉🥳')
