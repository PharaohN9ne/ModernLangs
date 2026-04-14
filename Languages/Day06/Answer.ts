//question1
const yourName: string = "Bob";
let yourAge: number = 22;
const buildWebApps: boolean = true;

console.log(yourName, yourAge, buildWebApps);

//question2
const passwordLength: number = 8;

if (passwordLength < 8) {
    console.log("Password too short")
}
else {
    console.log("Password length okay")
}

//question3
const tasks: string[] = ["Welcome to the store", "How can I help you?", "I'm looking for a mask"]

for (const task of tasks) {
    console.log(task);
}

//question4
function addTax(price: number, taxRate: number): number {
    return price + (price * taxRate);
}

let result = addTax(100, .06)
console.log(result)

//question5
const status: string = "outside";

function showStatus(): void {
    const status: string = "inside"
    console.log(status);
}

showStatus()
console.log(status)