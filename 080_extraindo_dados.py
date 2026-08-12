pos = 0
total = 0
numbers = []

while True:

    #input
    valor = int(input(f'Qual valor {pos+1}°?  '))
    numbers.append(valor)
    pos += 1

    #verifica se é verdade
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Continuar? [S/N]  ')).strip().upper()

    if cont == 'N':
        break

print('*/'*40)
#Calculo.
#ver quantos elementos foram digitados.;
print(f'Foi inserido {len(numbers)} elementos nessa listagem.')

#ver os numeros em ordem de tras pra frente usar o SORTED (NOME LISTA , REVERSE=TRUE);
print(f'Ordem decrescente são {sorted(numbers, reverse=True)}')

#ver se existe um número especifico na lista;
if 5 in numbers:
    print('O número 5 existe na lista')
else:
    print('O número 5 não foi adicionado.')