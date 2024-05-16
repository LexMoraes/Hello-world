programa {

	//Objetivo: Ler dois números e um operador matemático (+, -, *, /) e realizar a operação correspondente.
	
  funcao inicio() {
    inteiro num1
    inteiro num2
    cadeia operador
    inteiro resultado

    escreva("Digite um número: ")
    leia(num1)

    escreva("Digite um dos caracteres para escolher um dos operadores aritméticos:\nAdição(+);\nSubtração(-);\nMultiplicação(*);\nDivisão(/);\n\nEscolha: ")
    leia(operador)

    escreva("\nDigite outro número: ")
    leia(num2)

    se(operador == "+") {
      resultado = num1 + num2
      escreva("O resultado é: ", resultado)
    } senao se(operador == "-") {
      resultado = num1 - num2
      escreva("O resultado é: ", resultado)
    } senao se(operador == "*") {
      resultado = num1 * num2
      escreva("O resultado é: ", resultado)
    } senao se(operador == "/") {
      resultado = num1 / num2
      escreva("O resultado é: ", resultado)
    } senao {
    		escreva("Operador inválido")
    }


  }
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 459; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */