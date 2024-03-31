programa {
  inclua biblioteca Texto --> txt
  funcao inicio() {
  //Objetivo: Ler um CPF (apenas os números) e verificar se contém 11 dígitos
  
  cadeia cpf
  inteiro tamanho
  

  escreva("Digite apenas os números do seu CPF: ")
  leia(cpf)

  tamanho = txt.numero_caracteres(cpf)

  se (tamanho == 11) {
  	escreva("CPF válido")
    
  }




  }
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 352; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */