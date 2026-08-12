#082: 
# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

#qtd_itens será o primeiro input
qtd_itens = int(input('Quantos valores quer adicionar? '))
#listas
total_list = []
par_list = []
impar_list = []

#usando o for e com o "qtd_itens" fará o loop de 0 até qtd_itens ou...ex: 0 até 5
for i in range(0, qtd_itens):
    qtd_itens = int(input(f'Qual o {i+1}° valor: '))
    total_list.append(qtd_itens)

print('-'*40)
print(f'{"Resultado":^30}')
print('-'*40)
#total da lista.
print(f' 📋 Lista com todos os números {total_list}')
# total da lista pares e impares e conforme o IF o resultado é guardado
# demtro de uma nova lista
for x in total_list:
    if x % 2 == 0:
        par_list.append(x)
    elif x % 2 == 1:
        impar_list.append(x)

print(f' ➡️ Pares {par_list}')
print(f' ➡️ Ímpares {impar_list}')

