#Escreva um programa que pergunte o salário e calcule o aumento.
#salário > 1250.00 aumenta 10%
#salário <= 12500 aumenta 15%

print('* ' * 30)
####
sal = float(input("Informe seu salário atual R$ "))
salvalor = f'R$ {sal:_.2f}'
salvalor = salvalor.replace('.', ',').replace('_', '.')
####
##### Aumento 10 calcula na primeira linha, segunda linha formata para exibir, terceira: troca o PONTO, VIRGULA e UNDERLINE.
aumento10 = (sal * 0.10) + sal
aument010f = f'R$ {aumento10:_.2f}'
aument010f = aument010f.replace('.', ',').replace('_', '.')
####
aumento15 = (sal * 0.15) + sal
aumento15f = f'R$ {aumento15:_.2f}'
aumento15f = aumento15f.replace('.', ',').replace('_', '.')
####
print('* ' * 30)
print('Análisando o aumento...')
print('- ' * 30)
if sal > 1250:
    print(f'Com 10% - considerando seu salário de atual {salvalor} - valor novo {aument010f}')
else:
    print(f'Com 15% - considerando seu salário de atual {salvalor} - valor novo {aumento15f}')
