import time as t

print('='*30)
print('Calculadora de IMC (e peso ideal)')
print('='*30)
t.sleep(1)
peso = float(input("Qual o seu peso? (kg) "))
altura = float(input("Qual a sua altura? "))

imc = peso / ( altura * altura)
print('Agurde... ')
t.sleep(2)
print(f'Seu IMC é de {imc:.2f} kg/m2')

if imc <= 18.5:
    print('Abaixo do peso!!')
elif imc >= 18.6 and imc <= 24.9:
    print('Peso ideal')
elif imc > 25 and imc <= 29.9:
    print('Levemente acima do peso')
elif imc >  30 and imc <= 34.9:
    print('Obesidade grau 1')
elif imc > 35  and imc <= 39.9:
    print('Obesidade grau II (Severa)')
else:
    print('Obesidade III')