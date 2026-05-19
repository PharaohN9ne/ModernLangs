// Question 1

fn main() {
    let favorite_foods = vec!["apple", "papaya", "dragonfruit"];
    println!("{:?}", favorite_foods);
    println!("{}", favorite_foods[0]);
    println!("{}", favorite_foods[2]);
}

//Question 2

fn main() {
    let user_profile = ("Josh", 22, false);
    println!("{:?}", user_profile);
}

//Question 3

#[derive(Debug)]
struct Book {
    title: String,
    author: String,
    pages: u32,
}

fn main() {
    let book = Book {
        title: String::from("Apple"),
        author: String::from("Steve Jobs"),
        pages: 549,
    };

    println!("{:?}", book);
    println!("{}", book.title);
}

//Question 4

use std::collections::HashSet;

fn main() {
    let skills = HashSet::from([
        "boxing",
        "Muay Thai",
        "karate",
        "Muay Thai",
        "kickboxing",
    ]);

    println!("{:?}", skills);
    println!("{}", skills.contains("boxing"));
}

//Question 5
#[derive(Debug)]
struct Student {
    name: String,
    languages: Vec<String>,
    active: bool,
}

fn main() {
    let student = Student {
        name: String::from("Mike"),
        languages: vec![
            String::from("English"),
            String::from("Spanish"),
            String::from("French"),
        ],
        active: true,
    };

    println!("{:?}", student);
    println!("{:?}", student.languages);
}