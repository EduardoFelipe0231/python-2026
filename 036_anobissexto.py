import datetime

print('-=-' * 40)
print('Veja se o ano é Bissexto ou não..')
ano = int(input("Qual o ano?"))

if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano informado {ano} é Bissexto!!")
else:
    print(f"O ano {ano} não Bissexto.")
print('-=-' * 40)
print('Fim')

a = 3 * 5 + 4 ** 2

print(a)