# validar os possíveis tipos

txt = input('Digite algo: ')

print('Qual o tipo?', type(txt))
print('É número?', txt.isnumeric())
print('É alfabético?', txt.isalpha())
print('É minúscula?', txt.islower())
print('É Maiúscula?', txt.isupper())

