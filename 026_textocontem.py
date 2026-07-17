#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

#texto = str(input("Digite qual cidade você nasceu? "))

#escolha = texto.strip().lower().find('santo')

#print(f'A cidade escolhida foi {texto} e {escolha}')


texto = str(input("Digite sua cidade? ")).strip()

textodigitado = texto.upper().split()[0]

verifica = 'RIO' in textodigitado

print(f'{verifica}')