package Day12

import (
	"fmt"
)

//question 1

func main() {
	favoriteFoods := []string{"chicken", "goat", "beef"}
	fmt.Println(favoriteFoods)
}

//question 2

func main2() {
	userProfile := [3]string{"Bob", "52", "True"}
	fmt.Println(userProfile)
}

//question 3

func main3() {
	book := map[string]interface{}{
		"title":  "Apple",
		"author": "Steve Jobs",
		"pages":  549,
	}

	fmt.Println(book)
	fmt.Println(book["title"])
}

//question 4

type Book struct {
	Title  string
	Author string
	Pages  int
}

func main4() {
	book := Book{
		Title:  "Apple",
		Author: "Steve Jobs",
		Pages:  549,
	}

	fmt.Println(book)
	fmt.Println(book.Title)
}

//question 5

type Student struct {
	Name      string
	Languages []string
	Active    bool
}

func main5() {
	student := Student{
		Name:      "bob",
		Languages: []string{"English", "Spanish", "French"},
		Active:    true,
	}

	fmt.Println(student)
	fmt.Println(student.Languages)
}
