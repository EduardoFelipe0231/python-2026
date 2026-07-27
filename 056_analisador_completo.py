print('*-'*40)
print(' Analisador de dados')
print('*-'*40)

lista_nome = []
lista_idade = []

cont_idade = 0
cont_sexo = 0

for p in range(2):
    print(f'----- {p+1} Pessoa ----- ')
    nome = str(input('Nome: ')).strip().lower()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    todo = [nome, idade, sexo]
    lista_nome.append(todo)
    lista_idade.append(idade)

    #verifica de acordo com as informações cadastradas. idade menor 20 e sexo f.
    if idade <= 20 and sexo in 'Ff':
        cont_idade += 1
        cont_sexo += 1

    #pega a idade e divide pelo total de números na lista - pegando a média de idade.
    media_idade = (sum(lista_idade) / len(lista_idade))

    #verifica o homem mais velho e a sua idade.
    maior_idade = max(lista_idade)

    

print('*'*40)
print(' - Resultado - ')
print('*'*40)

## exibir média entre os valores.
print(f'A média de idade do grupo é de {media_idade} anos')

## Condição de exibir na tela do sexo e idade - 
if cont_sexo == 0:
    print('Nenhuma mulher cadastrada')
elif cont_sexo == 1:
    print(f'Temos {cont_sexo} mulher com menos de 20 anos')
else:
    print(f'Temos {cont_sexo} mulheres com menos de 20 anos')


