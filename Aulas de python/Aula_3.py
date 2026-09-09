exer = int(input("digite o numero do exercicio: "))
erro = True
import random

#Exer 1
if (exer == 1):
    cargo = input("Digite o cargo: ")
    valor = float(input("Digite o valor do salario: "))
    if(valor <= 3000 or cargo == "G"):
        print("Aumento de 10%")
    else:
        print("Aumento de 17%")
#Exer 2
elif (exer == 2):
    try:
        num = float(input("Digite um numero entre 10 e 50: "))
        if ((num >= 10) and (num <= 50)): # ou if num >= 10 and num <= 50:
            print(f"O numero {num} está entre 10 e 50 :)")
        else:
            print(f"O numero {num} não está entre 10 e 50 :(")
    except:
        print("Digite um numero valido >:(")
#Exer 3
elif (exer == 3):
    nome = input("Digite o nome do aluno: ")

    while erro == True:
        try:
            nota1 = float(input("Digite a primeira nota: "))
            nota2 = float(input("Digite a segunda nota: "))
            nota3 = float(input("Digite a terceira nota: "))
            erro = False
        except:
            print("Digite uma nota valida >:(")
    
    media = (nota1+nota2+nota3)/3

    presenca = float(input("Digite a porcentagem de presença do aluno: "))

    if media >= 6 and presenca >= 75:
        print(f"O aluno {nome} Foi aprovado! :) \n Com media {media:.0f} na nota e {presenca:.0f}% de presença.")
#Exer 4
elif (exer == 4):
    valor_base = float(input("Digite o valor da cobrança: "))
    parcelas = int(input("Digite a quantidade de parcelas: "))
    idade = int(input("Digite a idade do cliente: "))
    if(idade >= 60):
        print("O cliente é preferencial e não terá juros.")
        resultado = valor_base/parcelas
        print(f"O valor de R${valor_base:.2f} será parcelado em {parcelas} resultando em {parcelas}x de R${resultado:.2f} cada.")
    else:
        print("O cliente não é preferencial e terá juros.")
        juros = int(input("Digite a porcentagem dos juros: "))
        resultado = (valor_base+(valor_base * (juros/100)))/parcelas
        print(f"O valor de R${valor_base:.2f} será parcelado em {parcelas} com juros de {juros}% resultando em {parcelas}x de R${resultado:.2f} cada.")
#Exer 5
elif (exer == 5):
    print("!!! TABUADA !!!")
    num1 = int(input("Digite o primeiro numero da tabuada: "))
    num2 = int(input("Digite o segundo numero da tabuada: "))
    i = 0
    while (i <= num2):
        print(f"{num1} x {i} = {num1*i}")
        i += 1
    print("FIM DA TABUADA")
#Exer 6
elif (exer == 6):
    i= 1
    nota = 0
    while i <= 4:
        nota += float(input(f"Digite a {i}° Avaliação: "))
        i+= 1
    nota = nota/(i-1)
    print(f"A avaliação do estabelecimento é {nota:.1f}")
#Exer 7
elif (exer == 7):
    i = 1
    high_num = 0
    while i <= 25:
        random_num = random.randint(1, 100)
        print(f"{i}° numero gerado: {random_num}")
        i += 1
        if random_num > high_num:
            high_num = random_num
    print(f"O maior numero aleatorio gerado foi {high_num}.")
#Exer 8
elif (exer == 8):
    i = 1
    nota = 0
    alunos = int(input("Digite a quantidade de alunos: "))
    while i <= alunos:
        nota += float(input(f"Digite a nota do {i}° aluno: "))
        i += 1
    media = nota/alunos
    print(f"A nota media da sala de {alunos} alunos é {media:.1f}.")
else: #FIM DO CODIGO
    print("Não tem esse exercicio")
