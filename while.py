##################################

'''#x = 5

#while x <= 5: #condicao
    #print(x) #mostra
    #x += 1 #soma a cada loop que passar ele adicionar +1 no X, até a condição ser verdadeira.
'''

##################################
'''a = 0

while a <= 20:
    if a % 2 ==0:
        print(a, "- par")    
    a += 1'''

##################################
'''c = 1

while c != 0:
    c = int(input('Valor: '))
print('FIM')'''

##################################

'''r = 'S'

while r == 'S':
    texto = str(input(f'Digite algo..'))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
print('FIM')'''

##################################

continuar = 'S'

par = impar = 0
total = 0

while continuar == 'S':
    valor = int(input('Digite um valor: '))
    continuar = str(input('Continuar? [S/N] ')).strip().upper()
    if valor % 2 == 0:
        par += 1
    else:
        impar += 1

    total += 1
print(f'Dos {total} números informados, {par} são pares e {impar} é ímpares')
print('GG.')

