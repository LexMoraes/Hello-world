programa
{	//QuestÃ£o 6 - jogo pedra, papel e tesoura
	inclua biblioteca Util --> ut
	inclua biblioteca Texto --> txt

	funcao inicio()
	{
	inteiro pedra = 1
	inteiro papel = 2
	inteiro tesoura = 3
	inteiro npc //computador
	inteiro vc //usuário
	inteiro jogo // partidas
	inteiro vencidas = 0
	inteiro empate = 0
	inteiro derrota = 0
	
  escreva("Quantas partidas quer jogar?: ")

	leia(jogo)

	limpa()
		
	para(inteiro vez = 1; vez <= jogo; vez++) {

		escreva("Escolha: pedra(1), ou papel(2), ou tesoura(3) e que o melhor vença!\nEscolha: ")
		leia(vc)

		npc = ut.sorteia(1, 3)
    
		
	    	se (npc == vc) {
				empate+=1
							
			} senao se ((npc == 1 e vc == 2) ou (npc == 2 e vc == 3) ou (npc == 3 e vc == 1)) {
				vencidas+=1
				
			} senao se ((npc == 11 e vc == 3) ou (npc == 2 e vc == 1) ou (npc == 3 e vc == 2)) {
				derrota+=1
		
		}
		
	} escreva("Você escolheu jogar ", jogo," partida(as)!\nVenceu: ",vencidas,"\nPerdeu: ", derrota,"\nEmpatou: ",empate,"\n")
	
	}
}