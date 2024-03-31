programa {

	//Criar um algoritmo para criar um triângulo retângulo
	
  funcao inicio() {
    
    inteiro nivel
    cadeia altura = " * "
   
    escreva("digite uma quantidade para a altura: ")
    leia(nivel)

    para (inteiro n = 1; n <= nivel; n++) {
      
      para (inteiro q = 1; q <= n; q++) {
        escreva("* ")
      }

      escreva("\n")


    }
  }
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 67; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */