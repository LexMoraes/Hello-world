package main

import (
	"fmt"
	"main/variaveis"
	"main/vetores"
)

func main() {
	fmt.Println(variaveis.Age)
	fmt.Println(variaveis.Name)
	fmt.Println(variaveis.Ismarried)
	fmt.Println(vetores.Genero[0])

	var pessoa = vetores.Person{}
}
