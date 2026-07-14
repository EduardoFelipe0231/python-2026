print('---------------- Cotação de moedas ----------------')

real = float(input("Digite o seu valor em R$ "))

dolar = real * 5.15
euro = real *  5.87
libra = real * 6.88
iene = real * 0.03

print('Valor digitado BRL{:.2f} \n USD {:.2f} \n € {:.2f} \n £ {:.2f} \n ¥ {:.3f}'.format(real, dolar, euro, libra, iene))