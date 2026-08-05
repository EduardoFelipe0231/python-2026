#68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random

print('-'*40)
print(' VAMOS JOGAR PAR OU IMPAR? ')
print('-'*40)

ganhou = 0

while True:
    player = int(input('Diga um valor: '))
    #caso o usuário digitar número acima de 10, ele encerra o programa.
    if player > 10:
        print('Somente números até 10, vamos começar novamente')
        break

    #gera os números aleatórios de 0 a 10.
    computador = random.randint(0, 10)

    total = player + computador
    pergunta = str(input('Par ou Impar? [P/I]')).strip().upper()

    #caso não for P ou I na pergunta se é par ou ímpar ele encerra o programa.
    if pergunta not in 'PIpi':
        print('Somente [P ou I] é aceito, tente novamente.')
        break

    # IF em linha
    resultado_divisao = 'PAR' if total % 2 == 0 else 'IMPAR'

    #mostra o resultado.
    print('*'*50)
    print(f'Você jogou {player} e o computador {computador}. o total deu {total} é {resultado_divisao}')
    print('*'*50)

    # valida de acordo com a pergunta P ou I e com o resultado da soma!
    # % 2 == 0 'verifica se é par'
    # % 2 == 1 'verifica se é impar'
    if pergunta == 'P' and total % 2 == 0:
        print('Você GANHOU!!')
        print('Vamos jogar novamente...')  
    elif pergunta == 'I' and total % 2 == 1:
        print('Você GANHOU!!')
        print('Vamos jogar novamente...')
    else:
        print('Você PERDEU')
        print(f'Jogo acabou, até mais! ganhou {ganhou} vezes ')
        break
    #soma enquanto acertar com base nas condições acima dos IFs.
    ganhou +=1
    print('-'*50)
  





