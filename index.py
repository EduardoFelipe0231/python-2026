#ingressos = 120
#compradores = 170

#tem_ingressos_suficiente = (ingressos >= compradores)

#print(tem_ingressos_suficiente)

# ------------------------- Variáveis ------------------------- #

    # nome = input("Digite seu nome:")
    # idade = int( input("Digite sua idade:") )

# ------------------------- print com concatenação ------------------------- #

    # print ('Olá', nome, 'Você tem', idade , 'anos de idade' )

# ------------------------- validar o tipo da variável ------------------------- #
    # print (type(idade))

    # idade = 19

    # if idade >= 18:
    #     print("Está liberado")
    # else:
    #     print("Menor de idade!!")

# ------------------------- validando o salário -------------------------  #    

    # sal = 10

    # if sal <= 100:
    #     print("Valor menor que 100!")
    # elif sal > 100 and sal <= 200:
    #     print("Valor entre 100 e 200")
    # else:
    #     print("Valor maior que 200!!")

    # print(sal)

# ------------------------- média ------------------------- #

    # nota1 = 10
    # nota2 = 6
    # media = (nota1 + nota2) / 2

    # if media >= 7:
    #     print("Aprovado!!")
    # elif media <7 and media >= 5:
    #     print("Tem uma chance ainda!!")
    # else:
    #     print("Reprovado!")

    # print(media)


# ------------------------- array - listas ------------------------- #

    # array_numbers = [0, 2, 5, 10, 32, 40, 24, 66]

    # print("Maior número:", max(array_numbers))
    # print("Menor número:", min(array_numbers))
    # print("Total:", len(array_numbers))


# ------------------------- NOTAS ------------------------- #

# #Array para armazenar os dados
# notas = []

# #loop que irá receber os dados
# for x in range(2):
#     nome = input("Nome:")
#     codigo_aluno = input("RM: ")
#     nota_aluno = float (input ("Notas: "))
#     #essa lista irá aguardar os dados digitados acima, e logo irá adicionar o conteúdo na lista "resultados", que irá adicionar em outra lista "notas"
#     resultado = [nome, codigo_aluno, nota_aluno]
#     notas.append(resultado)

# #printa na tela a quantidade notas inseridas
# print("Quantidade de notas", len(notas))


# for n in notas:
#     nome = n[0]
#     codigo_aluno = n[1]
#     nota_aluno = n[2]
#     print("O Aluno(a)", nome , "RM:", codigo_aluno , "Tiro a nota de:" , nota_aluno)


# ---------- LISTA DE CONVIDADOS ---------------- #

    # lista_convidas = []

    # for c in range(3):
    #     nome_convidado = input("Digite seu nome:")
    #     dia_festa = input("Digite o dia:")

    #     result = [nome_convidado, dia_festa]
    #     lista_convidas.append(result)

    # print("Total de cadastrados", len(lista_convidas))


    # for r in lista_convidas:
    #     nome_convidado = r[0]
    #     dia_festa = r[1]
    #     print("O convidado do dia:", dia_festa, "é o:", nome_convidado)


# -------------- MOSTRANDO NOME -------------- #

#nome = input("Digite seu nome:")
#idade = int (input("Qual a sua idade?"))
#peso = float (input("Qual o seu peso?"))

#print('Olá' , nome, 'Você tem', idade , 'Anos de idade', 'e pesa' , peso, 'Kilos')