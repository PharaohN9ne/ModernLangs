//Question1
fn main () {
    let name = "Anthony";
    let age = 32;
    let wants_web_apps = true;

    println!("{} {} {}", name, age, wants_web_apps);
}

//Question2
fn main () {
    let password_length = 8;

    if password_length < 8 {
        println!("Password too short");
    }
    else {
        println!("Password length okay");
    }
}

//Question3
fn main () {
    let tasks = ["buy an apple", "pick up billy", "wash hair"];

    for task in tasks {
        println!("{}", task);
    }
}

//Question4
fn add_tax (price: i32, tax_rate: i64) {
    let final_price = price + (price * tax_rate);
}
fn main () {
    let x = add_tax(100, 0.06);
    println!("{}", x);
}

//Question5
fn main () {
    let status = "outside";
    {
        let status = "inside";
        println!("{}", status);
    }
    println!("{}", status);
}