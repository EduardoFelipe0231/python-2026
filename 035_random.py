import random
#numero do jogador
numero = int(input("Digite um numero de 0 a 10: "))

#numero do computador de 0 a 10
aleatorio = random.randint(0,10)

#condição IF caso o valor não for dentro do range ele não deixa o usuário seguir,
#caso for o jogo continua

print('Processando...')
5

if numero > 10:
    print("Ops.. você precisa digitar entre 0 a 10 apenas.")
else:
    if numero == aleatorio:
        print(f'Você acertou o número digitado {numero} - é igual ao da máquina {aleatorio}')
    else:
        print('O número digitado é diferente, tente novamente!')