exer = int(input("digite o numero do exercicio: "))

#Exer 1
if (exer == 1):
    lista = ["Pá", "Vassoura", "Rodo", "Pano de chão", "balde"]
    for produto in lista:
        print(produto)

#Exer 2
elif (exer == 2):
    lista = ["Pá", "Vassoura", "Rodo", "Pano de chão", "balde"]
    print(lista[1]) #não esqueça que o indice de uma lista sempre começa em 0

#Exer 3
elif (exer == 3):
    lista = ["Pá", "Vassoura", "Rodo", "Pano de chão", "balde"]
    del(lista[0])
    for i in lista:
        print(i)

#Exer 4
elif (exer == 4):
    lista = []
    lista.append("Flanela")
    for i in lista:
        print(i)

#Exer 5
elif (exer == 5):
    numbers = []
    i = 1
    while i <= 10:
        numbers.append(int(input(f"Digite o {i}° numero: ")))
        i += 1
    num_max = 0
    """ for num in numbers: """
    for num in range(10):
        if num_max < num:
            num_max = num
    print(f"O maior numero dentro da lista é {num_max}.")

#Exer 6
elif (exer == 6):
    num1 = int(input("Digite o numero da tabuada: "))
    num2 = int(input("Até que numero a tabuada deve ir?: "))

    print(f"!!!TABUADA DO {num1} ATÉ O {num2}!!!")
    for i in range(num2):
        print(f"{num1} X {i+1} = {num1*(i+1)}")
    print("!!!FIM DA TABUADA!!!")

#Exer 7
#Faça um programa que peça dois numeros, base e expoente, calcule e mostre o primeiros numero elevado ao segundo numero. Não utilize a função de potencia da linguagem.
elif (exer == 7):
    res = num = int(input("Digite o numero base: "))
    expo = int(input("Digite o expoente: "))
    for i in range(expo - 1):
        res = res * num
    print(f"O número {num} elevado a {expo} é igual a {res}.")
else: #FIM DO CODIGO
    print("Não tem esse exercicio")