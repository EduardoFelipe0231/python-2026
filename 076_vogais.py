#077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

print('-='*20)
print(f'{"VOGAL VERIFICANDO":^30}')
print('-='*30)
palavras = (str(input('Digite a primeira palavra: ')), str(input('Digite a segunda palavra: ')))
vogais = 'a','e','i','o','u'


#faz o for na tupla de palavras
for p in palavras:
    #mostra na tela as letras
    print(f'\n A palavra {p.upper()} temos as vogais: ', end= ' ')
    #faz o for na tupla das vogais
    for y in vogais:
        #verifica se no for das palavras existe algo das vogais.
        if y in p:
            print(f'{y}', end= ' -')           



        

        

    
