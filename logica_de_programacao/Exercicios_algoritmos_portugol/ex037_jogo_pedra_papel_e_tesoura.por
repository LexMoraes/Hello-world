programa
{	//Questão 6 - jogo pedra, papel e tesoura

	//Objetivo: Criar uma versão do jogo Pedra, Papel e Tesoura, onde o usuário joga contra o computador.
	//O usuário escolhe sua jogada digitando "Pedra", "Papel" ou "Tesoura", e o computador escolhe aleatoriamente.
	//O programa então determina o vencedor de cada rodada.

	inclua biblioteca Util --> ut
	
	funcao inicio()
	{
	inteiro pedra = 1 // Opção do jogo.
	inteiro papel = 2 // Opção do jogo.
	inteiro tesoura = 3 // Opção do jogo.
	inteiro npc // Escolha do jogador computador.
	inteiro vc // Escolhas do jogador usuário.
	inteiro jogo // Quantidade de partidas escolhidas para jogar.
	inteiro vencidas = 0 //Acumulador de vitórias.
	inteiro empate = 0 //Acumulador de empates.
	inteiro derrota = 0 //Acumulador de derrotas.
	
	
	escreva("Quantas partidas quer jogar?: ")
	leia(jogo) // número de vezes que o jogo percorrerá no laço.

	limpa() // limpa as interações anteriores.

	para (inteiro i = 0; i < jogo; i++) { // repetição para percorrer o jogo conforme a quantidade de partidas escolhidas.
		
		escreva("\nEscolha pedra(1), papel(2), ou tesoura(3) e que o melhor vença!\nEscolha: ") //Interação de escolha no jogo do jogador usuário.
		leia(vc) // Entrada de atribuição de escolha de jogo

		npc = ut.sorteia(1, 3) // método que escolhe aleatoriamente um jogo para o jogador computador.

		se(npc == 1) { // Bloco de condições para imprimir escolhas de jogo do computador
			escreva("\nComputador escolheu pedra\n")
		} senao se (npc == 2) {
			escreva("\nComputador escolheu papel\n")
		} senao se(npc == 3) {
			escreva("\nComputador escolheu tesoura\n")
		}
		
		se (npc == vc) { //Bloco de condições que define resultados da rodada
			empate = empate + 1	
		} senao se ((npc == 1 e vc == 2) ou (npc == 2 e vc == 3) ou (npc == 3 e vc == 1)) {
			vencidas = vencidas + 1	
		} senao se ((npc == 11 e vc == 3) ou (npc == 2 e vc == 1) ou (npc == 3 e vc == 2)) {
			derrota = derrota + 1
		}
	}
	escreva("\nVocê escolheu jogar ", jogo," partidas!\nVenceu: ",vencidas,"\nPerdeu: ", derrota,"\nEmpatou: ",empate,"\n") // Resultados
	
	}
}
