#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("Digite uma frase qualquer: ")).strip()
frase_usuario = str(input("Informe a letra que quer procurar? "))

procura = frase_usuario.lower().strip()
conta_letra = frase.count(procura)
primeira_letra = frase.find(procura)+1
ultima_letra = frase.rfind(procura)+1

print(f'A frase digitada foi "{frase}" - Veja a análise: \n A letra "{procura.upper()}" aparece {conta_letra}x na frase. \n A primeira letra {procura.upper()} aparece na posição {primeira_letra }°. \n A ultima letra {procura.upper()} aparece na posição {ultima_letra}°')