package functions

import (
	"fmt"
	Struct "main/struct"
)

var Contact []Struct.Phonebook

func AddContact() {

	for i := 0; i < len(Contact); i++ {
		fmt.Println("Insert the name of contact:")
		fmt.Scanln(&Contact[i].Name)

		fmt.Println("Insert the last name of contact:")
		fmt.Scanln(&Contact[i].LastName)

		fmt.Println("Insert a phone number:")
		fmt.Scanln(&Contact[i].Phone)

		Contact = append(Contact, Contact[i])
	}
}

func DeleteContact(i int) {
	Before := Contact[:i]
	After := Contact[i+1:]
	Contact = append(Before, After...)
}

func ListContact() {
	var Contact []Struct.Phonebook
	for i := 0; i < len(Contact); i++ {
		fmt.Println("Contact n", i+1, Contact[i])
	}
}
