#57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
while True:
    sex = str(input('Digite o seu sexo [M/F]: ')).strip().upper()
    if sex in 'fmFM':
        if sex == 'M':
            print(f'O sexo informado foi Masculino 🙍‍♂️')
        else:
            print(f'O sexo informado foi Feminino 💁‍♀️')
        break
    else:
        print(f'Valor digitado não é válido, tente novamente.')

print('Finalizou.')

    

