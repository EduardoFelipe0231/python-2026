numero = int(input('Informe um número: '))

c = numero
f = 1
print(f'Calculando o fatorial de {numero}! = ')
while c > 0:
    print(c, end=' ')
    print(' x ' if c > 1 else ' = ', end= '')
    f *=c
    c -= 1
print(f)