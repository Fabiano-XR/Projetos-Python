exer = int(input("digite o numero do exercicio: "))

#Exer 1
if (exer == 1):
    print("Hello World!!")
#Exer 2
elif (exer == 2):
    num = int(input("Digite um numero:"))
    if (num < 10):
        print(f"{num} é menor que 10.")
    elif (num > 10):
        print(f"{num} é maior que 10")
    else:
        print("O numero é igual a 10!.")
#Exer 3
elif (exer == 3):
    num1 = int(input("Digite o primeiro numero:"))
    num2 = int(input("Digite o segundo numero:"))
    if (num1 > num2):
        print(f"O maior numero é {num1}")
    elif (num1 < num2):
        print(f"O maior numero é {num2}")
    else:
        print(f"{num1} é igual a {num2}")
#Exer 4
elif (exer == 4):
    num1 = float(input("Digite o primeiro numero:"))
    num2 = float(input("Digite o segundo numero:"))
    media = (num1 + num2)/2
    if (media < 6):
        print(f"A média é {media:.2f} e o aluno foi reprovado.")
    else:
        print(f"A média é {media:.2f} e o aluno foi aprovado.")
#Exer 5
elif (exer == 5):
    sal = float(input("Digite o seu salário: "))
    if (sal <= 3000):
        new_sal = (sal*0.01) + sal
        print(f"Seu salário foi de R${sal:.2f} para R${new_sal:.2f}.")
    elif (sal <= 7000):
        new_sal = (sal*0.07) + sal
        print(f"Seu salário foi de R${sal:.2f} para R${new_sal:.2f}.")
    else:
        new_sal = (sal*0.15) + sal
        print(f"Seu salário foi de R${sal:.2f} para R${new_sal:.2f}.")
#Exer 6
elif (exer == 6):
    altura = float(input("Digite a altura da parede: "))
    largura = float(input("Digite a largura da parede: "))
    area_parede = largura * altura
    tinta = area_parede/3
    print(f"Para uma parede de {area_parede:.1f}m³ serão necessarias {tinta:.1f} latas de tinta.")
else: #FIM DO CODIGO
    print("Não tem esse exercicio")
