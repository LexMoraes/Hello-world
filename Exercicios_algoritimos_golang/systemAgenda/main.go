package main

import (
	"fmt"
	"main/functions"
)

var Choise int

func Menu() {
	fmt.Println("-----------------------------------------------------")
	fmt.Println("- This is the Phonebook. What do you want to do?:   -")
	fmt.Println("- [1]. Add a new contact:                           -")
	fmt.Println("- [2]. See contacts:                                -")
	fmt.Println("- [3]. Delete a contact:                            -")
	fmt.Println("- [4]. Close Phonebook:                             -")
	fmt.Println("-----------------------------------------------------")
}

func ChoiseMenu() {

	switch Choise {

	case 1:
		functions.AddContact()

	case 2:
		functions.ListContact()

	case 3:
		functions.DeleteContact()

	default:
		fmt.Println("Choise a number between 1 and 4")

	}
}

func main() {
	for {
		Menu()
		ChoiseMenu()
		if Choise == 0 {
			break
		}
	}
}
