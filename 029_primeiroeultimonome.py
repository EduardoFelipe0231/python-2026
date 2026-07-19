nome = str(input("Informe seu nome: ")).strip().title()

primeiro = nome.split()[0]
ultimo = nome.split()[-1]


print("Análisando o nome...")
print(f'O nome digitado é {nome.upper()}. \n \n Primeiro nome é {primeiro}. \n Ultimo nome é {ultimo}.')