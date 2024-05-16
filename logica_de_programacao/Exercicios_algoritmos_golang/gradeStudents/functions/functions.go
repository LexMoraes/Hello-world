package functions

import (
	"fmt"
	"main/structs"
)

func Menu() {
	fmt.Println("This is the database of students")
	fmt.Println("What do you wanna do?:")
	fmt.Println(
		"[1]: Sign a student\n" +
			"[2]: See the grades\n" +
			"[3]: See the total average\n" +
			"[4]: Exit of program\n")
}

var Classs []structs.Student
Turma[] = append(Turma, Pearson)

func AddStudent() {
	var Pearson structs.Student
	fmt.Println("Write the name of student:")
	fmt.Scan(&Pearson.Name)
	fmt.Println("Write the first grade of student:")
	fmt.Scan(&Pearson.Rate1)
	fmt.Println("Write the second grade of student:")
	fmt.Scan(&Pearson.Rate2)
	fmt.Println("Write the third grade of student:")
	fmt.Scan(&Pearson.Rate3)
	fmt.Println("Write the fourth grade of student:")
	fmt.Scan(&Pearson.Rate4)
}

func ListStudentsAndGrates() {
	for i := 0; i < len(Classs); i++ {
		fmt.Println("Name:", Classs[i].Name)
		fmt.Println("Rate1:", Classs[i].Rate1)
		fmt.Println("Rate2:", Classs[i].Rate2)
		fmt.Println("Rate3:", Classs[i].Rate3)
		fmt.Println("Rate4:", Classs[i].Rate4)
	}
}

func ChoiseMenu() {

	var Choise int32
	fmt.Scan(&Choise)

	switch Choise {
	case 1:
		AddStudent()
		break
	case 2:
		ListStudentsAndGrates()
		break
	default:
		fmt.Println("Erro, the choise don't have choise in menu")
	}

}
