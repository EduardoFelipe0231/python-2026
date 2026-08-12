#80: 
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista.
# já na posição correta de inserção (sem usar o sort()). 
# No final, mostre a lista ordenada na tela.

num_list = []
c = 0

for c in range(0, 5):
     valor = int(input(f'Digite a entrada {c+1}°: '))

if c == 0 or c > num_list[-1]:
    num_list.append(valor)
    print('Adicionado ao final da lista')
else:
    pos = 0
    while pos < len(num_list):
        if c <= num_list[pos]:
            num_list.insert(pos, c)
            print(f'Adicionado na posição {pos} da lista')
            break            
        pos +=1
        
print(f'Os valores digitados em ordem foram {num_list}')
    