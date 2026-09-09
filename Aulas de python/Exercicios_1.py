exer = 5 #int(input("digite o numero do exercicio: "))

#Exer1
if (exer == 1):
    print("")
#Exer2
elif (exer == 2):
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) /(10)
    print(f"A media ponderada é {media:.1f}")
#Exer 3
elif (exer == 3):
    distancia = float(input("Digite a distância Percorrida(KM): "))
    consumo = float(input("Digite o consumo de combustivel (KM/L): "))
    preco = float(input("Digite o preço do combustivel R$"))

    gasto = (distancia/consumo) * preco
    print(f"Em uma viagem de {distancia:.2f}km com um consumo de {consumo:.1f}Km/l e o preço do combustivel a R${preco:.2f} você gastou R${gasto:2f} nessa viagem.")
#Exer 4
elif (exer == 4):
    cap = float(input("Digite o valor do investivel incial: R$"))
    taxa = float(input("Digite a taxa anual: "))
    time = float(input("Digite o tempo de investimento (em anos): "))
    montante = (cap * (1 + taxa)) ** time
    print(f"Com o capital incial de R${cap:.2f} e a taxa de anual de {taxa}%. \n Em {time} anos o investimento final será de R${montante:.2f}")
#Exer 5 Escreva um programa que calcule o tempo (em horas, minutos e segundos) necessário para 
    # baixar um arquivo, dado o tamanho do arquivo (em MB) e a velocidade da conexão (em MB/s).
elif (exer == 5):
    speed = 1#float(input("Digite a velocidade da conexão (em MB/s): "))
    size = float(input("Digite o tamanho do arquivo (em MB): "))
    result = round(size/speed, 0)
    if result < 60:
        print(f"Levou {result:.0f} segundo(s).")
    elif result < 3600:
        print(f"Levou {round(result/60, 0)} minuto(s) e {result} segundos.")
        #print(f"Levou {result:.0f} minuto(s).")
    else:
        print(f"Levou {round((result/60)/60, 0)} hora(s){round(result/60, 0)} minuto(s) e {result} segundos.")
        #print(f"Levou {result:.0f} hora(s).")
else: #FIM DO CODIGO
    print("Não tem esse exercicio")
    valor_final = valor+(valor*0.1)