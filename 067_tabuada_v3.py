print('-'*50)
print(f' TABUADA ')
print('-'*50)
soma = 1

while True:
    tabuada = int(input('Qual tabuada gostaria de ver?? '))
    if tabuada <= 0:
        break
    else:
        print(' ------- RESULTADO -------')
        for i in range (1, 11):
            resultado = tabuada * i
            print(f'{tabuada} x {i} = {resultado}')   
        
        resposta = str(input('Deseja ver outra [S/N]? ')).strip().upper()

        if resposta == 'N':
            break     

    soma += 1
print('Foi encerrado, volte logo. 👏 :) ')
