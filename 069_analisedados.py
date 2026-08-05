#69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A - quantas pessoas tem mais de 18 anos.
#B - quantos homens foram cadastrados.
#C-  quantas mulheres tem menos de 20 anos.
import time

#variáveis
soma_age = 0
soma_gender = 0
soma_woman = 0
soma_total = 0 

while True: 
    print('=-'*40)
    print('CADASTRE UMA PESSOA')
    print('=-'*40)      
    age = int(input('Qual a idade? '))   

    if age <= 0 or age >= 120:
        print('Insira uma idade válida, tente novamente')
        break

    #if para o caso do  KEEP
    gender = ' '
    while gender not in 'FM':
        gender = str(input('Qual o sexo [F/M]?  ')).strip().upper()

    #if para o caso do  GENDER
    keep = ' '
    while keep not in 'SN':
        keep = str(input('Continuar [S/N]? ')).strip().upper()    

    if keep == 'N':
        break
    
    soma_age += 1
    soma_total += 1
    soma_gender += 1
    soma_woman += 1    

print(' =========== FIM DO CADASTRO =========== ')
time.sleep(1)
print('📊 Analisando os dados...')
time.sleep(1)
print(f'Total de pessoas cadastradas {soma_total+1} pessoas.')
time.sleep(2)

print('⏳ Carregando mais informações ')
time.sleep(2)
# IF validação da idade.
if age >= 18:
    print(f' ➜ Total de pessoas com mais de 18 anos: {soma_age}')
else:
    print(' ➜ Não foi cadastradas pessoas acima ou igual a 18 anos.')

# IF validação masculino cadastrados.,
if gender == 'M':
    print(f' ➜ Temos {soma_gender} com o sexo masculino')

if gender == 'F' and age <=20:
    print(f'Ao total temo {soma_woman} mulher com menos de 20 anos.')
