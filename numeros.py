num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
print('-'*30)

maior_primeiro = num1 > num2
maior_segundo = num2 > num1



if maior_primeiro:
    print(f"O primeiro número é maior",)
elif maior_segundo:
    print(f"O segundo número é maior",)
else:
    print("Os números são iguais")

