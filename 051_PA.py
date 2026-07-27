print('´'*50)
print('progressão aritmética')
print('´'*50)

termo = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))

print('=-'*50)

for i in range(10):
    pa = termo + razao * i
    print(f'{pa}', end=' > ')
print('Finalizou')