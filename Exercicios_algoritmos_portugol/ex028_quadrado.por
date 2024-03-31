programa {
  funcao inicio() {
    
    inteiro nivel
    cadeia altura = " * "
   
    escreva("Entre com uma quantidade de altura: ")
    leia(nivel)

    para (inteiro n = 1; n <= nivel; n++) {
      
      para (inteiro q = 1; q <= nivel; q++) {
        escreva(" * ")
      }

      escreva("\n")


    }
  }
}
