#Desenvolva um programa que pergunte a distância de uma viagem em KM.
#Calcule o preço da passagem, cobrando RS 0,50 por Km para viagens de até 200km.
#e RS 0,45 por viagens mais longas

distancia = float(input("Digite quantos Km a será a viagem: "))
cidade = str(input("Qual será o destino? ")).strip()

curta = distancia * 0.60
longa = distancia * 0.45

if distancia <= 200:
    print(f"A viagem com destino para {cidade} será de {distancia:.2f} km - Confira o valor total para pagamento: \n O preço será R$ {curta:.2f}.")
else:
    print(f"A viagem com destino para {cidade} será de {distancia:.2f} km - Confira o valor total para pagamento: \n O preço será R$ {longa:.2f}.")


