num = int(input("Digite um valor de 0 a 1.000.000: "))
print(f"Analisando o número digitado {num} ")

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
dm = num // 10000 % 10
cm = num // 100000 % 10
mil = num // 1000000 % 10

print(f"O número {num} tem \n Unidade: {u} \n Dezena: {d} \n Centena {c} \n Milhar {m} \n Dezena milhar {dm} \n Centena Milhar {cm} \n Milhão {mil}")
