nome = input('Digite seu nome: ')
carro = input('Informe o modelo do carro:')
dias = int(input('Digite quantos dias ficou com o carro? '))
km = float(input(f'Informe a kilometragem percorrida nesse periodo de {dias} dias?'))

km_price = 0.15
dia_price = 60



total_pagar = (dia_price * dias) + (km_price * km)

print(f'Olá {nome} 👋!! \n Você alugou o modelo {carro} por {dias} dias e andou o total de {km:.2f} km rodados')
print('*'*60)
print(f'Aqui está o total que deve ser pago, confira: \n 👉🏼 dias: {dias} \n km: {km:.2f} \n 💲 total é de R$ {total_pagar}')