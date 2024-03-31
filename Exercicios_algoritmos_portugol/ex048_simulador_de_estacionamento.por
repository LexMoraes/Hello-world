programa {

	//Crie um algoritmo que simule vagas em um estacionamento, casa posição equivale a uma placa estacionada. Abaixo algumas regras do algoritmo:
	//1. Verificar se a vaga já está ocupada
	//2. Verificar se o mesmo veículo já não está estacionado
	//3. Deve ser possível remover um veículo do estacionamento
	//4. Listar todas as vagas ocupadas
	//5. Tempo que o carrro esteve estacionado

	
  inclua biblioteca Calendario
  inclua biblioteca Util

  cadeia vagas[5] = {"dispo","dispo","dispo","dispo","dispo"}
  inteiro horasEntrada[5]
  inteiro vaga

  funcao inteiro totalEmSegundos(inteiro hora, inteiro minuto, inteiro segundo){
    inteiro totalSegundos = (hora * 3600) + (minuto * 60) + segundo
    retorne totalSegundos
  }

  funcao cadeia formatarHorario(inteiro totalSegundos) {
    inteiro horas = totalSegundos/3600
    inteiro minutos = (totalSegundos%3600)/60
    inteiro segundos = totalSegundos%60 
    retorne horas + " hrs: " + minutos + " min: " + segundos + " seg"
  }

  funcao vazio exibirMenu(){
  escreva ("\n\nEste é o estacionamento da FPF Tech. O que você quer fazer?")
  escreva ("\n[1] Estacionar veículo:")
  escreva ("\n[2] Verificar disponibilidade do estacionamento:")
  escreva ("\n[3] Retirar veículo:")
  escreva ("\n[4] Deseja sair do programa?:")
  escreva ("\nEscolha: ")
  }
  	
  funcao vazio addVeiculo(cadeia placa, inteiro vaga) {
 	 se(vagaOcupada(vaga) == falso) {
		se (placaEstacionada(placa) == falso) {
    			vagas[vaga] = placa
      		inteiro hora = Calendario.hora_atual(falso)
			inteiro minuto = Calendario.minuto_atual()
    			inteiro segundo = Calendario.segundo_atual()

    			horasEntrada[vaga] = totalEmSegundos(hora, minuto, segundo) 
    			
    			escreva("\nEstacionamento concluído") 
		} senao {
			escreva("\nVeículo já estacionado")
		} 
 	 } senao {
		escreva("\nVaga ocupada")
    	}
    }
  
  funcao logico vagaOcupada(inteiro vaga) {
    retorne (vagas[vaga] != "dispo")
  }

  funcao logico placaEstacionada(cadeia placa) {
    para (inteiro i = 0; i < 5; i++) {
      se(vagas[i] == placa) {
        retorne verdadeiro
      }
    }
    retorne falso
  }

  funcao vazio removerVeiculo(cadeia placa) {
    para(inteiro i = 0; i <= 4; i++) {
      se(vagas[i] == placa) {
        vagas[i] = "dispo"
        inteiro hora = Calendario.hora_atual(falso)
        inteiro minuto = Calendario.minuto_atual()
        inteiro segundo = Calendario.segundo_atual()

        inteiro horarioSaida = totalEmSegundos(hora, minuto, segundo)

        inteiro diferenca = horarioSaida - horasEntrada[i]

        escreva("O veículo ficou no estacionamento: ", formatarHorario(diferenca))
      }
    }
  }

  funcao vazio listarVagas() {
    para (inteiro i = 0; i < 5; i++) {
      escreva("\n Vaga ",i+1,": ", vagas[i])
    }
  }
  
  
  funcao inicio() {
  
  inteiro acao = 0
  cadeia placa
	faca {
  	exibirMenu()
  	leia(acao)

  	escolha(acao) {
    	caso 1:
      escreva("\nInsira a placa do veículo: ")
      leia(placa)
      escreva("\nExistem 5 vagas enumeradas de zero(0) à quatro(4)\nInsira a vaga que deseja estacionar: ")
      leia(vaga)
      addVeiculo(placa, vaga)
      pare

    	caso 2:
      listarVagas()
      pare

    	caso 3:
      escreva("Qual a placa do veículo que você quer retirar?: ")
      leia(placa)
      
      removerVeiculo(placa)
      pare
  	}
  	
	} enquanto(acao != 4)

  }

}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 545; 
 * @DOBRAMENTO-CODIGO = [17, 38, 61, 70, 87];
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */