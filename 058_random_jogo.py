#58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
import time


pc = random.randint(0,10)
tr = 0

print(''' ******* BEM VINDO AO JOGO DE ADIVINHA, É VOCÊ CONTRA A MÁQUINA *******''')

time.sleep(0.5)

while True:
    time.sleep(0.5)
    player = int(input('👉 Adivinhe o valor qu estou pensando!! digite entre 0 a 10: '))

    print('Jogando o dado 🤔💭🎲...')

    time.sleep(1)

    if player == pc:
        print(f'Acertou com {tr+1} tentativas, Parabéns você ganhou!! 🎯🎉 ------------ ')
        break

    elif player > pc:
        print("Quase, você jogou um número maior")
    else:
        print("Número menor, tente novamente")

    

    time.sleep(0.5)

    tr += 1 #contador de vezes jogadas
    

print(' ----------- JOGO ACABOU ----------- ')