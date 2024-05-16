programa {

	//Objetivo: Ler um número inteiro e determinar se é par ou ímpar.

  funcao inicio() {
    inteiro num

    escreva("Digite um número inteiro: ")
    leia(num)

    se(num%2 == 0 e num > 0) {
      escreva("O número ", num, " é par.")
    } senao se (num == 0){
      escreva("O número ", num, " é nulo.")
    } senao se (num%2 != 0) {
      escreva("O número ", num, " é ímpar.")
    }
     
  }
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 78; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */