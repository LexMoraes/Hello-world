package main

//Crie um algoritmo que simule vagas em um estacionamento,
// cada posição equivale a uma placa estacionada.
// Abaixo algumas regras do algoritmo:
//1. Verificar se a vaga já está ocupada
//2. Verificar se o mesmo veículo já não está estacionado
//3. Deve ser possível remover um veículo do estacionamento
//4. Listar todas as vagas ocupadas
//5. Tempo que o carrro esteve estacionado

import (
	"fmt"
	"main/crud"
)

func main() {

	crud.Parking[0] = "Available"
	crud.Parking[1] = "Available"
	crud.Parking[2] = "Available"
	crud.Parking[3] = "Available"
	crud.Parking[4] = "Available"

for {

		crud.ShowMenu()

		fmt.Scan(&crud.Choice)

		switch crud.Choice {
		case 1:

			fmt.Println("Insert the plaque of vehicle:")
			fmt.Scan(&crud.Plaque)
			fmt.Println("Insert the vacancy that you want:")
			fmt.Scan(&crud.Vacancy)

			crud.AddV()
			break

		case 2:
			crud.ShowVacancy()
			break
		case 3:
			var remove string
			fmt.Println("Insert the plaque of vehicle:")
			fmt.Scan(&remove)

			crud.RemovePlaque(remove)
			break

		case 4:

		}
		if crud.Choice == 0 {
			break
		}
	}
}
