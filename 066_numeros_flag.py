n = s = c = 0

while True:
    n = int(input('Informe um número [ 999 ou 0 para parar]:'))
    if n == 0 or n == 999:
        break #para o programa
    s += n 
    c += 1




    
print(f' ============== FIM ============== ')
print(f'Foi digitado {c} números - a soma entre eles são {s}')
