print('*'*40)
print('\033[95m Tabela de números primos de 0 a 100')
print('\033[m*'*40)

numero = 13
num_lista = []

for i in range(1, numero+1):
    if numero % i == 0:
        print()