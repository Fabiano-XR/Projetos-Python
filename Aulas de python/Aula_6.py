import re, os, random

exer = 18
#exer = input("Digite um exercício: ")

if exer == 1:
    padrao = re.compile(r'[0-9]{4}')  #input("Digite um padrão: ")

    texto = "O pedido 5832 foi enviado para o setor 47."

    first_resultado = re.search(padrao, texto)
    print(f"Primeiro resultado: {first_resultado.group()}")
    resultados = re.findall(padrao, texto)
    print(f"Todos os resultados: {resultados}")

elif exer == 2:
    padrao = re.compile(r'[\w]+[@][\w]+[.][\w]+')
    texto = "O contato informado pelo cliente foi atendimento@exemplo.com."

    print(f"Todos os resultados: {re.findall(padrao, texto)}")

elif exer == 3:
    padrao = re.compile(r'[\d]{2}[/][\d]{2}[/][\d]{4}')
    texto = "A atividade foi marcada para 18/09/2026, às 19 horas."

    resultado = re.findall(padrao, texto)
    print(f"A data é {resultado}")

elif exer == 4:
    texto = "O produto selecionado possui o código ABC-4821 e está disponível."
    padrao = re.compile(r"[A-Z]{3}[-][\d]{4}")

    resultado = re.search(padrao, texto)
    print(f"O codigo é {resultado.group()}")

elif exer == 5: #exercicio de debug
    #import re 
 
    #padrao = r"[0-9]+" 
    padrao = r"[0-9]{4}"
    #Se colocar "+" ele identifica qualquer um com 1 ou mais em vez de exatamente "4" numeros

    texto = "Os pedidos 5832 e 7419 foram enviados para o setor 47." 
    
    encontrado1 = re.search(padrao, texto) 
    encontrado2 = re.findall(padrao, texto) 
    
    print(encontrado1) 
    print(encontrado2)

elif exer == 6: #exercicio de debug
    #import re 
 
    padrao = r"\S+@\S+\.\S+" 
    
    texto = "O e-mail informado foi aluno@exemplo.com" 
    
    #encontrado1 = re.search(texto, padrao) 
    #encontrado2 = re.findall(texto, padrao) 
    encontrado1 = re.search(padrao, texto) 
    encontrado2 = re.findall(padrao, texto)
    #Primeiro deve vir o padrão a ser procurado e depois oque

    print(encontrado1) 
    print(encontrado2)

elif exer == 7:
    texto = """ 
    Mariana realizou sua inscrição no evento. 
    E-mail informado: mariana.silva@email.com 
    
    Carlos ainda não confirmou sua participação. 
    E-mail informado: carlos_22@exemplo.com.br 
    
    A inscrição de Fernanda foi confirmada. 
    E-mail informado: fernanda99@teste.org 
    """ 
    padrao = r'[\w]+[@][\w]+[.][\w]+'

    resultado = re.search(padrao, texto)
    resultados = re.findall(padrao, texto)

    print(f"O primeiro email encontrado é {resultado.group()}")
    print(f"Todos os emails encontrados são {resultados}")

elif exer == 8:
    padrao = re.compile(r"\d{4}")
    texto = """ 
    Machado de Assis (1839-1908) - escritor brasileiro. 
    Contato: machado.assis@literatura.com 
    Cidade: Rio de Janeiro - RJ 
    
    Carolina Maria de Jesus (1914-1977) - escritora brasileira. 
    Contato: carolina.jesus@literatura.com 
    Cidade: Sacramento - MG 
    
    Conceição Evaristo (1946) - escritora brasileira. 
    Contato: conceicao.evaristo@literatura.com 
    Cidade: Belo Horizonte - MG 
    
    Carlos Drummond de Andrade (1902-1987) - poeta brasileiro. 
    Contato: carlos.drummond@literatura.com 
    Cidade: Itabira - MG 
    """
    resultados = re.findall(padrao, texto)
    print(f"Anos encontrados são: {resultados}")

elif exer == 9:
    texto = """ 
    Biblioteca Machado de Assis 
    Telefone: (21) 3456-7821 
    Cidade: Rio de Janeiro - RJ 
    
    Biblioteca Carolina Maria de Jesus 
    Telefone: (11) 2987-4512 
    Cidade: São Paulo - SP 
    
    Biblioteca Cora Coralina 
    Telefone: (62) 3678-9012 
    Cidade: Goiânia - GO 
    
    Biblioteca Graciliano Ramos 
    Telefone: (82) 3123-7788 
    Cidade: Maceió - AL"""
    padrao = r"\(\d{2}\) \d{4}-\d{4}"
    resultados = re.findall(padrao, texto)
    print(f"Os numeros encontrados são: {resultados}")

elif exer == 10: #exercicio de debug
    #import re 
 
    #padrao = r"\([0-9]{2}\) [0-9]{5}-[0-9]{4}"
    padrao = r"\([0-9]{2}\) [0-9]{4}-[0-9]{4}" 
    #Numero de de vezes q deveria procurar o numero incorreto, alterado de 5 para 4
    
    texto = """ 
    Biblioteca Central 
    Telefone: (11) 3456-7821 
    
    Biblioteca Municipal 
    Telefone: (21) 2876-4512 
    
    Biblioteca Universitária 
    Telefone: (31) 3678-9012 
    """ 
    
    encontrado1 = re.search(padrao, texto) 
    encontrado2 = re.findall(padrao, texto) 
    
    print(encontrado1) 
    print(encontrado2)

elif exer == 11:
    caminho = os.path.dirname(os.path.abspath(__file__)) #onde ta o script
    arquivo = os.path.join(caminho,"arquivos", "protocolos.txt") #adiciona onde quero ir
    with open(arquivo, "r", encoding="utf-8") as f:
        texto = f.read()
    print(f"O conteudo do arquivo é {texto}")

    padrao = r"AT-\d{4}-\d{4}"
    protocolos = re.findall(padrao, texto)

    print(f"Os protocolos são: {protocolos}")

elif exer == 12:
    caminho = os.path.dirname(os.path.abspath(__file__))
    arquivo = os.path.join(caminho,"arquivos", "erros.txt")
    with open(arquivo, "r", encoding="utf-8") as f:
        texto = f.read()
    padrao = r"ERRO-\d{3}"
    erros = re.findall(padrao, texto)
    print(f"Os erros foram: {erros}")

elif exer == 13:
    caminho = os.path.dirname(os.path.abspath(__file__))
    arquivo = os.path.join(caminho,"arquivos", "acessos_1.txt")
    with open(arquivo, "r", encoding="utf-8") as f:
        texto = f.read()

    padrao = r"(?<==)[a-z0-9_]+"
    usuarios = re.findall(padrao, texto)
    print(f"Os usuarios do sistema são: {usuarios}")
    
elif exer == 14:
    caminho = os.path.dirname(os.path.abspath(__file__))
    arquivo = os.path.join(caminho,"arquivos", "programa.txt")
    with open(arquivo, "r", encoding="utf-8") as f:
        texto = f.read()
    padrao = r"[A-Z]+"
    categorias = re.findall(padrao, texto)
    print(f"As categorias são: {categorias}")

elif exer == 15: #exercicio de debug
    #import re 

    caminho = os.path.dirname(os.path.abspath(__file__))
    arquivo = os.path.join(caminho,"arquivos", "erros.txt")
    padrao = r"ERRO-[0-9]{3}" 
    
    with open(arquivo, "r", encoding="utf-8") as f: 
        #texto = f 
        texto = f.read()
        #Faltava o .read() para que possa ler oq tem em f

    encontrado = re.findall(padrao, texto) 
    
    print(encontrado)

elif exer == 16:
    #Descreva o funcionamento do programa e qual será o seu resultado
    numeros = [] 
 
    for i in range(10): 
        numero = random.randint(0, 999999) 
        numeros.append(numero) 
    
    with open("numeros_1.txt", "w", encoding="utf-8") as arquivo: 
        for i in range(len(numeros)): 
            arquivo.write(f"{numeros[i]}\n") 
    
    with open("numeros_1.txt", "r", encoding="utf-8") as arquivo: 
        texto = arquivo.read() 
    
    print(texto)
    #gera 10 numeros aleatorios, escreve eles em numeros.txt e depois lê o arquivo e mostra na tela

elif exer == 17:
    caminho = os.path.dirname(os.path.abspath(__file__))
    arquivo = os.path.join(caminho,"arquivos", "acessos_2.txt")

    sucesso = []
    falha = []
    padrao1 = r".+SUCESSO$"
    padrao2 = r".+FALHA$"

    with open(arquivo, "r", encoding="utf-8") as f:
        texto = f.readlines()

        for linha in texto:
            linha = linha.rstrip()
            ocorrencia = re.search(padrao1, linha)
            if ocorrencia:
                sucesso.append(linha)
            else:
                falha.append(linha)

    print(f"\n Tivemos {len(sucesso)} acesso bem sucedidos.")
    for i in range(len(sucesso)):
        print(f"{sucesso[i]}\n")

    print(f"\n Tivemos {len(falha)} acesso com falhas.")
    for i in range(len(falha)):
        print(f"{falha[i]}\n")    

elif exer == 18:
    numero = maior_num = len_tres_alg = tres_alg = 0
    menor_num = 100000
    dois_alg = []
    quatro_alg = []
    
    script = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(script,"arquivos", "numeros_2.txt")

    #A)
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for i in range(1000):
            num = random.randint(0, 999999)
            arquivo.write(f"{num}\n")

    with open(caminho, "r", encoding="utf-8") as arquivo:
        texto = arquivo.readlines()

    #B)
    for i in texto:
        numero = int(i.strip())
        
        if maior_num < numero:
            maior_num = numero
        if menor_num > numero:
            menor_num = numero

        ocorrencia = 0
        ocorrencia = re.search(r"^\d{2}$", i.strip())
        if ocorrencia:
            dois_alg.append(ocorrencia.group())
        else:
            ocorrencia = re.search(r"^\d{3}$", i.strip())
            if ocorrencia:
                tres_alg = int(ocorrencia.group())
                len_tres_alg +=1
            else:
                ocorrencia = re.search(r"^\d{4}$", i.strip())
                if ocorrencia:
                    quatro_alg.append(ocorrencia.group())

    result_tres = tres_alg/len_tres_alg

    print(f"O maior numero é {maior_num}")
    print(f"O menor numero é {menor_num}")
    print(f"Foram encontrados {len(dois_alg)} numeros com dois algarismos.")
    print(f"A uma media de {result_tres:.0f} numeros com tres algarismos.")
    print(f"Foram encontrados {len(quatro_alg)} numeros com quatro algarismos.")


    
