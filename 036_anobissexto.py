import time

print('-=-' * 40)
print('Veja se o ano é Bissexto ou não..')
ano = int(input("Qual o ano?"))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano informado {ano} é Bissexto!!")
else:
    print("Ano não Bissexto.")
print('-=-' * 40)
print('Fim')