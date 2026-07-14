largura = float(input("Qual a largura da sua parede? "))
altura = float(input("Qual a altura da sua parede?"))

metros = largura * altura
tinta = metros / 2

print('Sua parede tem {}x{} - {:.2f}m²'.format(largura, altura, metros))
print('Para pintura a parede você precisaria de {:.2f}l'.format(tinta))