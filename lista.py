# ------------------------------------------------------------------------------- #
                    # LISTA AULA 01
# ------------------------------------------------------------------------------- #
# ----------------------- #
   ## METODO LIST ##
# ----------------------- #

'''
    valores = list(range(1, 11))

    print(valores)

    for i in valores:
        print(i)
'''

# ----------------------- #
   ## IN LIST ##
# ----------------------- #

#if 'chocolate' in lista:
    #lista.remove('chocolate')
    #print('Chocolate foi removido')
    #print(lista)
#else:
    #print('Não existe')
    #Print(lista)

# ----------------------- #
   ## ITENS ##
# ----------------------- #
#lista.pop()     <- exclui o ultimo
#lista.append()  <- adiciona no final
#lista.insert()  <- inseri em alguma posição
#lista.remove()
#del lista
#lista.sort()
#lista.sort(reverse=True)
# sorted

# ------------------------------------------------------------------------------- #
                    # LISTA AULA 02
# ------------------------------------------------------------------------------- #

# fabricantes = ['FIAT', 'CHEVROLET', 'VOLKSWAGEN']
# modelos = ['MOBI', 'CAMARO', 'SONG']
# fabricantes.append('BYD')


# modelos.append(fabricantes[:])

# print(modelos)


# ----- #
# LISTA COMPOSTAS

# pessoas = [['Pedro', 25], ['Maria', 19], ['João', 25]]

# print(pessoas[0][0])  # <-posição 0 da lista, posição 0 da pessoa,
# print(pessoas[1][0])
# print(pessoas[1])     # <- retorna todo os itens da posição 1 - MARIA  19
# o primeiro zero é a posição fora, e o seguindo é relacionado a posição dentro (pedro)

# [:] faz uma cópia da lista.

'''pessoas = [['Pedro', 23], ['Maria', 13], ['João', 27], ['Sara', 17],]

count_maior = 0
count_menor = 0

-------------------------------------------------------------------------------
### Exemplo 01 ###

for p in pessoas:
    if p[1] > 18:
        # print(f'{p[0]} tem {p[1]} anos de idade')
        count_maior +=1
    elif p[1] < 18:
        count_menor +=1

print(f'{"Resultado":-^30}')
print(f'Temos {count_maior} pessoas maiores de 18 anos \n Temos {count_menor} menor de 18')'''

# -------------------------------------------------------------------------------
### Exemplo 02 ###

#agrupado = []
#dados = []

#for i in range(0, 2):
    #dados.append(str(input('Nome: ')).strip().title())
    #dados.append(int(input('Idade: ')))
    #agrupado.append(dados[:]) # <- faz uma copia de dados.
    #dados.clear()          # <- apaga os dados ao final

#print("Total de pessoas: " , agrupado)

