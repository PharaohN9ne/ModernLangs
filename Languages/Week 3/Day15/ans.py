#question 1

name = "Charles"
favorite_language = "English"

print(f"My name is {name} and I can speak {favorite_language}.")

#question 2

question = "What is your name? "
answer = input(question)

print(f"Hello, {answer}!")

#question 3

with open("my_notes.txt", "w") as file:
    file.write("Hello World!\n")
    file.write("This is my first true line.\n")
    file.write("This is just a test.\n")

#question 4

with open("my_notes.txt", "r") as file:
    content = file.read()

print(content)

#question 5

tasks = ["Go to the store.", "Order a bag of chips.", "Open the store."]

with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")

with open("tasks.txt", "r") as file:
    for line in file:
        print(line.strip())