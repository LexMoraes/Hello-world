programa {

	//Objetivo: Ler três números e exibi-los em ordem crescente.
	
  funcao inicio() {
    inteiro num1, num2, num3
    inteiro aux
    escreva("Digite o primeiro número: ")
    leia(num1)

    escreva("Digite o segundo número: ")
    leia(num2)

    escreva("Digite o terceiro número: ")
    leia(num3)
    
    se(num1 > num2) {
      aux = num1
      num1 = num2
      num2 = aux
    } 
    se(num2 > num3) {
      aux = num2
      num2 = num3
      num3 = aux
    } se(num1 > num2) {
      aux = num1
      num1 = num2
      num2 = aux
    }
    escreva("A ordem decrescente é: ",num1,", ", num2,", ", num3)
  }
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 73; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */