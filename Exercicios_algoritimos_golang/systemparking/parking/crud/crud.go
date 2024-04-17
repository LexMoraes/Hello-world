package crud

import (
	"fmt"
)

var Choice int
var Plaque string
var Vacancy int
var Parking [5]string


func ShowMenu() {
	fmt.Println("---------------------------------------------------------------")
	fmt.Println("- Este é o estacionamento da FPF Tech. O que você quer fazer? -")
	fmt.Println("- [1] Estacionar veículo:                                     -")
	fmt.Println("- [2] Verificar disponibilidade do estacionamento:            -")
	fmt.Println("- [3] Retirar veículo:                                        -")
	fmt.Println("- [4] Deseja sair do programa?:                               -")
	fmt.Println("- Escolha:                                                    -")
	fmt.Println("---------------------------------------------------------------")
}

func IndexOccupied(Vacancy int) bool {
	if Parking[Vacancy] == "Avaliable"{
		return false
	}else{
		return true
	}
}

func PlaqueOccupied(Plaque string) bool {

	for _, Plaque := range Parking {
		return true
	}
	return false
}



func AddV() {
	if !IndexOccupied(Vacancy) && !PlaqueOccupied(Plaque) {
		Parking[Vacancy] = Plaque
	} else {
		fmt.Println("This vacancy isn't available or plaque already in vacancy")
	}
}

func ShowVacancy() {
	for i := 0; i < len(Parking); i++ {
		fmt.Println(Parking[i])
	}
}

func RemovePlaque(Vacancy int, Plaque string) {
	if Parking[Vacancy] == Plaque {
			Parking[Vacancy] = "Available"
		}
}
