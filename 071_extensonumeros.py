#72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

print('*'*40)
print('Leia um número')
print('*'*40)

#tuplas com os nomes por extenso.
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
extenso_US = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')


while True:
    num = int(input('Digite um valor de 0 a 20: '))

    #valida conforme condições < 0 ou > 20.
    if num < 0 or num > 20:
        print('Número inválido, tente novamente.')
        continue
    
    language = ' '
    while language not in 'USBR':          
          language = str(input('Deseja ver em qual idioma? [US / BR]')).strip().upper() 

    #valida o idioma entre US ou BR para traduzir o número digitado.
    if language == 'US':
        for cont in range(0, len(extenso_US)):
                if num == cont:
                    print(f'Você digitou o número {extenso_US[cont].upper()}')
    else:
        for cont in range(0, len(extenso)):
                if num == cont:
                    print(f'Você digitou o número {extenso[cont].upper()}')
                   
    #print(f'NUMERO DIGITADO FOI {extenso[num]}')
    #valida se não receber S ou N, não avança;
    next = ' '
    while next not in 'SN':
        next = str(input('Ver outro número? [S/N]')).strip().upper()

    if next == 'N':
        break    
    
print('fim')

     
    