#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.

#Quantas letras ao todo (sem considerar espaços).

#Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: "))

maiuscula = nome.upper()
minuscula = nome.lower()
primeiro_nome = len(nome.split()[0])
total = len(nome) - nome.count(' ')

print(f'Em Maiuscula >> {maiuscula}')
print(f'Em Minuscula >> {minuscula}')
print(f'Seu primeiro nome tem {primeiro_nome} letras')
print(f'O total de caracteres no seu nome é de {total} letras')