#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

import time

### Lê a nota
print("--------------- Bem vindo a média de notas 📝 ---------------")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print('Calculando...')
time.sleep(2)
print('-=-'*40)
print(f"👉 As notas informadas foram  {nota1:.0f} e {nota2:.0f}")
print('-=-'*40)
print('Verificando média 👀 🎯')
time.sleep(3)
print('Quase lá 😬')
time.sleep(4)

print('===== Resultado ===== ')

if media < 5:
    print(f"Sua média foi de {media}, você foi reprovado ☹")
elif 5 >=  media <= 6.9:
    print(f"Sua média foi de {media}, você está de recuperação ")
else:
    print(f"Parabéns você foi aprovado sua média foi de {media} 🎉🥳")