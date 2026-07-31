#68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random

print('-'*40)
print(' VAMOS JOGAR PAR OU IMPAR? ')
print('-'*40)

soma = 0

while True:
    player = int(input('Diga um valor: '))

    computador = random.randint(0, 10)

    total = player + computador


