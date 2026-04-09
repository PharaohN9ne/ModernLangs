#Question1
for count in range(1,6):
    print(count)

#Question2
tasks = ["go to the store", "make dinner", "pick up baby"]

for task in tasks:
    print(task)

#Question3
numbers = [1, 2, 3, 4, 5]
total = 0

for number in numbers:
    total += number

print(total)

#Question4
off = 3

while off > 0:
    print(off)
    off -= 1
print("Lift off!")

#Question5
temperatures = [75, 69, 19, 99, 21, 5]

for temperature in temperatures:
    if temperature < 20:
        print("Cold")
    else:
        print("Warm")