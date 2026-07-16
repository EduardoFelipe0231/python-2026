kg = float(input('Informe seu peso atual: '))

ml = 35
total_agua = kg * ml
litro = total_agua / 1000
copo = 300
total_copos = (copo / 1000 ) * (total_agua / 100 )

print(f'O seu peso é: {kg:.2f} Kg \n Você deve beber {total_agua} ml de água por dia 💧. \n Total de 🧴 {litro:.2f} L')
print('='*80)
print(f'Você precisa tomar {total_copos:.0f} copos de {copo} ml para bater a mete de {litro:.2f}')