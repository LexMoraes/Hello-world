programa {

  funcao real celsiusParaFahrenheit(real temperatura) //Defindo função para conversão de celsius para fahrenheit com tipagem 'real' e 'parâmetro' como temperatura
	{
		real f = temperatura * 9/5 + 32
		retorne f
  }

  funcao real FahrenheitParacelsius(real temperatura) //Defindo função para conversão de fahrenheit para celsius com tipagem 'real' e 'parâmetro' como temperatura
	{
		real c = (temperatura-32)*5/9
		retorne c
	}
  
  funcao inicio() {
  //Objetivo: Converter uma temperatura dada em Celsius para Fahrenheit ou vice-versa,
  //conforme a escolha do usuário.
  real temperatura
  cadeia escalatermo
  real fahrenheit
  real celsius
  


  escreva("Digite um número que corresponda a temperatura atual: ")
  leia(temperatura)

  escreva("Qual a escala termométrica desta temperatura? Digite e confirme uma das iniciais que represente a escala:\nCelsius(C);\nFahrenheit(F);\n")
  leia(escalatermo)

  se(escalatermo == "C" ou escalatermo == "c") { //Validação de escolha para celsius
    fahrenheit = celsiusParaFahrenheit(temperatura)
    escreva("Essa temperatura em Fahrenheit é: ", fahrenheit,"°F")

  } senao se (escalatermo == "F" ou escalatermo == "f") { //Validação de escolha para fahrenheit
    celsius = FahrenheitParacelsius(temperatura)
    escreva("Essa temperatura em Celsius é: ", celsius,"°C")
  } 
  
  senao se (escalatermo != "F" ou escalatermo != "f" ou escalatermo != "C" ou escalatermo != "c") {
  	escreva("Opção inválida")
  }
}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 206; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */