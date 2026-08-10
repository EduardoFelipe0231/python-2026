msg = 'BYD 2026 - TABELA'

print('*'*40)
print(f'{msg:^40}')
print('*'*40)

carros = ('Dolphin Mini GL', 106.000,
          'Dolphin Mini GS', 110.000,
          'King GL', 140.000,
          'Atto 8', 330.000,
          'Yuan Pro', 150.500)

# FORMA 1 UNPACKING USANDO LISTA + TUPLA

#for nome, preco in carros:
    #print(f'{nome:.<30} R$ {preco:.3f}')

# FORMA 2 USANDO FOR com a TUPLAS

for i in range(0, len(carros)):
        if i % 2 == 0:
            print(f'{carros[i]:.<30}', end= '')
        else:
            print(f'R$ {carros[i]:>8.3f}')




# usar o :>30 para informar o tanto de espaço, tudo que tiver depois do ponto vai aparecer - e o < > ^ defini o alinhamento do texto ex: usar o < para deixar o texto na esquerda.