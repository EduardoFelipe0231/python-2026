print('*'*70)
print('Descubra quanto vale a tempera em Celsius em Kelvin ( K ) e fahrenheit ( °F )')

c = float(input('Informe a temperatura em ºC :  '))

f = int(9 * c / 5 + 32)
k = c + 273.15

print(f'A temperatura informado foi de {c} ºC 🌡️ - em {k} K - em {f:.1f} °F')