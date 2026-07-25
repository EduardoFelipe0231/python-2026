#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

#acumulador
soma = 0
#contador
cont = 0

for a in range(1, 501, 2):
    if a % 3 == 0:
        cont += 1
        soma += a
print(f'a soma total é de {soma} - e tem {cont} números somados.') 