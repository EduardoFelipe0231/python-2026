#Escreva um programa que leia uma velocidade do carro e informe se foi multado ou não.
#Para cada KM ultrapassado será pago 7 reais por KM a mais.

valor = int(input("Informe a velocidade: "))


máxima = 80
multa = ( valor - máxima ) * 7


if valor > máxima:
    print(f"Vixe, você foi multado!! A velocidade máxima era de {máxima} km/h - você estava a {valor} km/h - Sua multa será no total R$ {multa} reais")
print(f"Parabéns, a sua velocidade de {valor}km/h é compatível com a via!!")

