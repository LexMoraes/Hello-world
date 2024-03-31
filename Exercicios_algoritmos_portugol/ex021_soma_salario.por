programa {

  //programa esreva 5 salarios e retorne a soma dos 5
  
  funcao inicio() {
    real salario = 0
    real soma = 0

    para (inteiro c = 0; c <= 5; c++) {
      escreva("Digite seu salário: ")
      leia(salario)
      soma += salario
    }

    escreva("A soma dos 5 salários é: ", soma)
  }
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 282; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */