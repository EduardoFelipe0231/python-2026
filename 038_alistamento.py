import datetime as dt
import time

print('='*40)
print("Você pode se alistar? veja aqui")
time.sleep(1)
data = int(input("Qual o ano do seu nascimento? "))

today = dt.date.today().year
aniver = today - data
falta = 18 - aniver
alistamento = aniver + today
ano_alistamento = today + falta

str_faltam = "faltam" if falta > 1 else "falta"
str_ano = "Anos" if falta > 1 else "Ano"

print("Verificando...")
time.sleep(2)

print(f"Sua idade é {aniver} anos em {today}")

if aniver < 18:
    print(f"Você ainda não pode se alistar. {str_faltam} {falta} {str_ano} para se apresentar.\n Seu alistamento será em {ano_alistamento}")
elif aniver == 18:
    print("Alistamento já!!")
else:
    print("Você já não precisa mais se alistar")

print('Até mais!')
print('='*40)