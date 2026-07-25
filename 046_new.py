entrada = int(input('Quantas pessoas será cadastrada? '))

pessoas = []


for i in range(0, entrada):
    idade = int(input('idade: '))
    nome = str(input('nome: ')).strip().capitalize()
    print('-'*40)
    resultado = [nome, idade]
    pessoas.append(resultado)

print('='*40)
print(f'Total de pessoas cadastrada {len(pessoas)}')
print('='*40)

print('*'*30)

for n in pessoas:
    nome = n[0]
    idade = n[1]
    print(f'👉 Nome: {nome} Idade: {idade}', end='\n')


