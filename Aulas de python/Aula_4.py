exer = 2#int(input("digite o numero do exercicio: "))

#Exer 1
if (exer == 1):
    times = []
#    var = input("deseja adicionar um time? Y/N: ")
#    if var == "Y":
#        while (var == "Y") or (var == "y"):
#            times.append(input("Digite o nome do time: "))
#            var = input("deseja adicionar mais um time? Y/N: ")
#        print(times)

#Exer 2   O prefeito da cidade de Cabrobo do Fundo pensa em inovar nas proXimas eleicoes implantando urna eletronica e voce foi o programador escolhido para cumprir esta tarefa. O codigo devera colher o codigo do candidato, e contar mais um voto. No final do dia devera ser mostrado na tela o nome de cada candidato e o total  de votos alcaçando por cada um deles respectivamente. (Deve contar os Votos Brancos e Nulos)
elif (exer == 2):
    i = 1
    candidato_1 = 0
    candidato_2 = 0
    candidato_3 = 0
    branco = 0
    nulo = 0
    while i <= 10:
        candidato = int(input("Zé Bafo de Onça - 1 \n Mané Barnabé - 2 \n Bode Zé - 3 \n Voto em Branco - 4 \n Voto Nulo - 5 \n Digite o numero do candidato: "))
        if candidato == 1:
            candidato_1 += 1
            print("Obrigado pelo seu voto!")
            i += 1
        elif candidato == 2:
            candidato_2 += 1
            print("Obrigado pelo seu voto!")
            i += 1
        elif candidato == 3:
            candidato_3 += 1
            print("Obrigado pelo seu voto!")
            i += 1
        elif candidato == 4:
            branco += 1
            print("Obrigado pelo seu voto!")
            i += 1
        else:
            nulo += 1
            print("Obrigado pelo seu voto!")
            i += 1
    print(f"Candidatos ||||| Votos \n Zé Bafo de Onça - {candidato_1} \n Mané Barnabé - {candidato_2} \n Bode Zé - {candidato_3} \n Voto em Branco - {branco} \n Voto Nulo - {nulo}")
    
#Exer 3     
elif (exer == 3):
    a = 1
else: #FIM DO CODIGO
    print("Não tem esse exercicio")