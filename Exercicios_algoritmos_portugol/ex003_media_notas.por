programa {

	//Objetivo: Ler quatro notas, calcular a média e informar se o aluno está aprovado ou reprovado (considere 7 para aprovação).
	
  funcao inicio() {
  real nota1
  real nota2
  real nota3
  real nota4
  real somanota
  real media
    escreva("\nEste algoritimo lê duas notas de uma disciplina e retorna a média da nota")
    escreva("\nDigite uma das notas: ")
    leia(nota1)
    
    escreva("\nDigite a segunda nota: ")
    leia(nota2)

    escreva("\nDigite a terceira nota: ")
    leia(nota3)

    escreva("\nDigite a quarta nota: ")
    leia(nota4)

    somanota = nota1 + nota2 + nota3 + nota4
    media = somanota/4

    escreva("\nA média é: ", media)

    se(media >= 7) {
      escreva("\nVocê está aprovado!")
    } senao {
      escreva("\nVocê está reprovado.")
    }
  }
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 672; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */