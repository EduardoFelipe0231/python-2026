nome = str(input('Qual o seu nome? '))

acha = 'silva' in nome.strip().lower().split()

print(f'Seu nome tem Silva? {acha}')