package Day09

import "fmt"

//Question 1
func main1() {
	name := "Greg"
	age := 66
	buildWebApps := false

	fmt.Println(name, age, buildWebApps)
}

//Question 2
func main2() {
	var passwordLength int

	if passwordLength < 8 {
		fmt.Println("Password too short")
	}
	else {
		fmt.Println("Password length okay")
	}
}

//Question 3
func main3() {
	tasks := []string {"Take me to lunch", "grab dinner with the homie", "Buy sandwich"}

	for index, tasks := range tasks {
		fmt.Println(index, tasks)
	}
}

//Question 4
func addTax (price float64, taxRate float64) float64 {
	return price + (price * taxRate)
}

func main4()  {
	finalPrice := addTax(98.00, .08)

	fmt.Println(finalPrice)
}

//Question 5
func main5() {
	status := "outside"

	{
		status := "inside"
		fmt.Println(status)
	}

	fmt.Println(status)
}