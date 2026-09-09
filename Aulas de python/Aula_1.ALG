Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 27/04/2026
Var
// Seção de Declarações das variáveis 
   num1, num2, op: inteiro
   res: real
Inicio
      escreval("Digite o primeiro número: ")
      leia(num1)
      escreval("Qual a operação desejada?")
      escreval("1 - Soma")
      escreval("2 - Subtração")
      escreval("3 - divisão")
      escreval("4 - Multiplicação")
      leia(op)
      escreval("Digite o segundo número: ")
      leia(num2)
      se op = 1 então
        res <- num1 + num2
        escreval(num1," +",num2," =",res)
      fimse
      se op = 2 então
        res <- num1 - num2
        escreval(num1," -",num2," =",res)
      fimse
      se op = 3 então
        res <- num1 / num2
        escreval(num1," /",num2," =",res)
      fimse
      se op = 4 então
        res <- num1 * num2
        escreval(num1," *",num2," =",res)
      fimse


Fimalgoritmo