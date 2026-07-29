import time

print(' ----- FAÇA SUA CONTA ----- ')

## Input
num_one = int(input('Primeiro valor: '))
num_two = int(input('Segundo valor: '))

#resultados
sum_total = num_one + num_two
sub_total = num_one - num_two
mult_total = num_one * num_two
div_total = num_one / num_two
major_total = (max(num_one, num_two))
minor_total = (min(num_one, num_two))

operation = 0

while operation != 9:
    time.sleep(2)
    
    print('''\033[1;31m
    ** Opções **

    [\033[1;31m 1 ] (+) Somar 
    [\033[1;31m 2 ] (-) Subtrair
    [\033[1;31m 3 ] (*) Multiplicar
    [\033[1;31m 4 ] (/) Dividir
    [\033[1;31m 5 ] (>) Maior
    [\033[1;31m 6 ] (<) Menor
    [\033[1;31m 7 ] (=) Comparação
    [\033[1;31m 8 ] (n) Novos números
    [\033[1;31m 9 ] Sair
             ''')
         
    operation = int(input('\033[0;0m Qual operação você deseja? '))
    
    print('⸝⸝・'*20)  
    if operation == 1:
        print(f'O resultado entre {num_one} + {num_two}: {sum_total}')
    elif operation == 2:
        print(f'O resultado entre {num_one} - {num_two}: {sub_total}')
    elif operation == 3:
        print(f'O resultado entre {num_one} x {num_two}: {mult_total}')
    elif operation == 4:
        print(f'O resultado entre {num_one} ÷ {num_two}: {div_total}')
    elif operation == 5:
        print(f'Entre {num_one},{num_two} o maior número é: {major_total}')
    elif operation == 6:
        print(f'Entre {num_one},{num_two} o menor número é: {minor_total}')
    elif operation == 7:
        if num_one == num_two and num_two == num_one:
            print('Número iguais')
        else:
            print('Os números informados são diferentes')
    elif operation == 8:
        num_one = int(input('Primeiro valor: '))
        num_two = int(input('Segundo valor: '))
    elif operation == 9:
         print('Programa encerrado! até mais 👋')
    else:
         print('Opção não existe, tente novamente.')   

    print('\033[0;0m⸝⸝・'*20)


