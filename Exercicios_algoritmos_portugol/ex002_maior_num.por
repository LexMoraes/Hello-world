programa {

	//Objetivo: Ler dois números inteiros e determinar qual é maior, menor ou se são iguais.
	
  funcao inicio() {
    inteiro num1
    inteiro num2
    escreva("Digite um número: ")
    leia(num1)
    
    escreva("Digite um segundo número: ")
    leia(num2)

    se (num1 > num2) {
      escreva(num1," é maior que ",num2)
    } senao se(num1 == num2) {
      escreva(num1," é igual ao ",num2)
    } senao
      escreva(num2," é maior que ",num1)
  }
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 292; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */