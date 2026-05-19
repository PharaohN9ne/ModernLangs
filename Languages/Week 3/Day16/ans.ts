//question 1

const name1: string = "Anthony";
const favoriteLanguage: string = "English";

console.log(`My name is ${name1} and I speak ${favoriteLanguage}.`);

//question 2

import * as readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

const rl = readline.createInterface({ input, output });

const name = await rl.question("What is your name? ");
console.log(`Hello, ${name}!`);

rl.close();

//question 3

import { writeFile } from "node:fs/promises";

await writeFile(
    "my_notes.txt",
    "Hello from TypeScript!\nThis is my second line.\nThis is the third line.\n",
    "utf8"
);

//question 4

import { readFile } from "node:fs/promises";

const content = await readFile("my_notes.txt", "utf8");
console.log(content);

//question 5

const tasks: string[] = ["Go to the store", "buy wine", "cook dinner"];

await writeFile(
    "tasks.txt",
    tasks.join("\n") + "\n",
    "utf8"
);

const tasksContent = await readFile("tasks.txt", "utf8");
const tasksLines = tasksContent.split("\n");

for (const line of tasksLines) {
    if (line.trim() !== "") {
        console.log(line);
    }
}