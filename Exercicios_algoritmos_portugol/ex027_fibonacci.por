programa {
  funcao inicio() {
    //Fazer a sequ�ncia de fibonacci no la�o
    inteiro termo1 = 0
    inteiro termo2 = 1
    inteiro quantidades_termos
    inteiro proximo

    escreva("Digite a quantidade de termos limite da sequ�ncia de fibonacci para ser mostrado: ")
    leia(quantidades_termos)

    para(inteiro n = 0; n <=quantidades_termos; n++) {
      proximo = termo1 + termo2
      escreva(termo1, " ")

      termo1 = termo2
      termo2 = proximo
    }
    
  }
}
