#Aprovando o imprestimo ou não.
import time

print('='*50)
print("Empréstimo bancário para sua casa dos sonhos, veja se irá conseguir!!!")
nome = str(input("Olá, digite seu nome completo para iniciar a consulta:")).strip()
print("Perfeito, um momento...")
time.sleep(2)
print(f"ótimo, Olá {nome} Bem-vindo!! Vamos lá, agora preciso saber de alguns detalhes ⬇ ")
casa = float(input("Qual o valor da casa? R$ "))
print('-'*30)
sal = float(input("Qual o seu salário atual? R$ "))
print('-'*30)
anos = float(input("Quanto tempo você quer pagar pelo imovel? "))
print("Maravilha, um momento...")
time.sleep(3)
print('Agora que já tenho seus dados, irei análisar se é possível você realizar esse processo.. um minuto.')
time.sleep(3)
print("Ok, aqui está as informações.")
##### Calculos...

tempo_ano = anos * 12  
parcelas = casa / tempo_ano
verifica = ( 30 / 100 ) * sal

print(f'{nome.upper()} para financiar uma casa de {casa:.2f} em {anos:.0f} a prestação mensal será de R$ {parcelas:.2f} por mês \n')
print(f'{verifica:.0f}')

if verifica >= parcelas:
        print('Parabéns, seu emprestimo foi aceito!!')
else:
    print("Infelizmente não é possível concluir esse emprestimo.")


