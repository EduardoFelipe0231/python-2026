#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
import datetime as dt

idade = int(input("Sua idade: "))

idade_atual = dt.datetime.today().year - idade

print(f'Sua idade é {idade_atual} anos você está no grupo:')
if idade_atual <= 9:
    print(f"Mirim")
elif idade_atual <= 14:
    print(f'INFANTIL')
elif idade_atual <= 25:
    print(f'SÊNIOR')
else:
    print(f'MASTER')