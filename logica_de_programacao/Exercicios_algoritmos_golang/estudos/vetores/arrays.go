package vetores

var escola = []string{"b", "a"}
var Genero = [2]string{"male", "female"}
var idades = [3]int{1, 2, 3}

type Person []struct {
	Name          string
	Age           int
	IsMarried     bool
	Salary        int
	OriginCountry string
}
