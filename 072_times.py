#73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

#Os 5 primeiros times.

#Os últimos 4 colocados.

#Times em ordem alfabética.

#Em que posição está o time da Chapecoense.

Times = ('Palmeiras','Flamengo','Athletico-PR','Fluminense','Bahia','Bragantino',
         'Cruzeiro','Botafogo','Corinthians','Atlético-MG','Coritiba','São Paulo',
         'EC Vitória','Mirassol','Santos','Internacional','Grêmio','Vasco da Gama',
         'Remo','Chapecoense')

print('*'*50)
print('Tabela do brasileirão 2026')
print('*'*50)

search = str(input('Qual time? quer ver? ')).strip().capitalize()

print('*----> Times presentes <----*')

for pos, t in enumerate(Times):
    print(f'{pos+1}ª........ {t}')

print('=-*'*40)
print(f'O seu time {search} está na {Times.index(search)+1}ª posição na tabela' )
print('=-*'*40)
print('=-'*40)
print(f'Os primeiros times são: {Times[:5]}')
print('=-'*40)
print(f'Os útlimos colocados são: {Times[-4:]}', sep= ', ')
print('=-'*40)
print(f'Lista em ordem alfabética: {sorted(Times)}')
print('=-'*40)

