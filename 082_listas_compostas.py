#084: 
# #Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. 
# #B) Uma listagem com as pessoas mais pesadas. 
# #C) Uma listagem com as pessoas mais leves.


### NAO FINALIZADO ###

todos = []
dados = []
maior = []

total_cad = 0

while True:
    # recebendo os dados
    nome = input('Nome da pessoa: ').strip().title()
    peso = int(input('Peso (Kg) : '))
    genero = str(input('Sexo [F/M]: ')).strip().upper()

    # adicionando os dados na lista dados.
    dados.append(nome)
    dados.append(peso)
    dados.append(genero)
    # adicionando os dados na lista dados.
    todos.append(dados[:])

    # Limpa os dados no final do loop.
    dados.clear()

    # pergunta se vai continuar;
    sair = ' '
    while sair not in 'SN':
        sair = str(input( ' CONTINUAR [S/N] ? ')).strip().upper()
    if sair == 'N':
        break

    # soma quatos foram adicionados.
    total_cad +=1

print('='*50)
print(f'Cadastrou {total_cad+1} pessoas')
print(f'Cadastrou {len(todos)}')

## Validando o maior peso
for i in range(0, len(todos)):
    maior.append(todos[i][1])
    

print(max(maior))