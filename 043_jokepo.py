import random
import time


print(f'{"JOKENPO o JOGO":=^30}')
print('''
👉 Pedra
👉 Papel
👉 Tesoura

''')
jogador = str(input("Qual sua escolha? ")).strip().lower()
opcoes = ["pedra", "papel", "tesoura"]
escolha = random.choice(opcoes)

time.sleep(1)
print('JO...')
time.sleep(1)
print('KEN...')
time.sleep(1)
print('POOÓ!!')

print('=-'*60)
if jogador == escolha:
    print(f'Empate')
elif jogador == 'pedra' and escolha == 'tesoura':
    print(f'Você não é nada máquina, hehe!! Vitória jogador 💪')
    print('Pedra 🗿 esmaga tesoura ✂️')
elif jogador == 'tesoura'  == 3 and escolha == 'papel':
    print(f'Você não é nada máquina, hehe!! Vitória jogador 💪')
    print('✂️ tesoura amassa 📃 papel')
elif jogador == 'papel' == 2 and escolha == 'pedra':
    print(f'Você não é nada máquina, hehe!! Vitória jogador 💪')
    print(f'📃 papel embrulha pedra 🗿')
elif escolha == 'pedra' and jogador == 'tesoura':
    print(f'HAHAHA, ganhei humano!! Vitória máquina 🤖')
    print('Pedra 🗿 esmaga tesoura ✂️')
elif escolha == 'tesoura' and jogador == 'papel':
    print(f'HAHAHA, ganhei humano!! Vitória máquina 🤖')
    print('✂️ tesoura amassa 📃 papel')    
elif escolha == 'papel' and jogador == 'pedra':
    print(f'HAHAHA, ganhei humano!! Vitória máquina 🤖')
    print(f'📃 papel embrulha pedra 🗿')
else:
    print('....')