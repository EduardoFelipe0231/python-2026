import time

print('-=-'*40)
print('   Progressão aritmética ')
print('-=-'*40)

primeiro = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))

contador = 1
print('Analisando..')
time.sleep(1)

print(f'📈 Aqui está o resultado da PA de termo {primeiro} e razão {razao}.')
while contador < 10:
    pa = primeiro + razao * contador
    contador +=1
    print(pa, end=' 👉 ')
print('end')
