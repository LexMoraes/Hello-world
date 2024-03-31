programa
{
	//Objetivo: criar um algoritmo para retornar o salário informado de uma pessoa do sexo masculino ou feminino.
	
	funcao inicio()
	{
		
		real salario = 0.0
		cadeia sexo
		cadeia continuar = "sim"

		faca {
		
			escreva("\nInforme o sexo da pessoa: \nMasculino (M):\nFeminino (F):\nDigite: ")
			leia(sexo)
	
			se(sexo == "M" ou sexo == "m") {
				sexo = "homem"
				escreva("\nInforme o salário: ")
				leia(salario)
				
				escreva("Essa pessoa é um(a) ", sexo, " e o salário é R$", salario)
				
				escreva("\nQuer continuar?:\nSim (S):\nNão (N):\nResponda: ")
				leia(continuar)
				
			}se(sexo == "F" ou sexo == "f") {
				sexo = "mulher"
				escreva("\nInforme o salário: ")
				leia(salario)
							
				escreva("Essa pessoa é um(a) ", sexo, " e o salário é R$", salario)
				
				escreva("\nQuer continuar?: Sim (S):\nNão (N):\nResponda: ")
				leia(continuar)
				
			} senao se (continuar != "S" ou continuar != "s" ou continuar != "f" ou continuar != "F")
				
				escreva("\nComando inválido")
					
		
		}enquanto (continuar == "S" ou continuar == "s")
				
	}
	
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 29; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */