sal = float(input('Qual o seu salário atual? '))


percent = 0.2
calc_sal = sal * percent

print(f'Salário atual de R$ {sal:.2f} reais, \n Com aumento de {percent: .0%}, ficaria R$ {sal + calc_sal:.2f} reais')