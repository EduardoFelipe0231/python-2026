print('========================= Porcentagem ========================= \n')

sal = float(input('Informe o seu salário atual? '))
percent = int(input('Qual a porcentagem? ' ))

print('------------ Resultado ------------ \n')

percent = percent / 100
calc_sal = sal * percent


print(f'Seu salário atual de R$ {sal:.2f} reais, \n Considerando os {percent: .0%} \n o novo valor seria de R$ {sal + calc_sal:.2f} reais')

print(percent)