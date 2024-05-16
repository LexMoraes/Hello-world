programa {
  funcao inicio() {
    //Objetivo: Ler um ano e determinar se é bissexto.
  inteiro ano

  escreva("Digite um ano: ")
  leia(ano)
  
  se(ano%4 == 0 e ano%100 != 0 ou ano%4 == 0 e ano%400 == 0) {
    escreva("O ano ", ano, " é bissexto")
  } senao {
    escreva("O ano ", ano, " não é bissexto")
  }
  

  }

}
