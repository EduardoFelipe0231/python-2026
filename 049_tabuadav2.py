#faça um programa que mostre a tabuada

print('*'*40)
print('TABUADA')
print('*'*40)

divisao = int(input('Qual tabuada deseja ver? '))

for tabuada in range (1, 11):
    resultado = divisao * tabuada
    print(f'{divisao} x {tabuada} = {resultado}')