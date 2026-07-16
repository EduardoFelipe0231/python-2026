# Calcular o valor do cateto oposto e adjacente e mostre na tela.

from math import hypot

co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente:"))

hi = hypot(co, ca)
#hi = (co ** 2 + ca ** 2) ** (1/2)

print(f"O valor da hipotenusa é: {hi:.2f}")
