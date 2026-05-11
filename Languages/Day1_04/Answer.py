#Question1
def say_hello():
    print("Hello!")

say_hello()

#Question2
def greet_person(name):
    print("Hello, " + name + "!")

greet_person("Bob")

#Question3
def multiply_numbers(num1, num2):
    return num1 * num2

#print(multiply_numbers(3, 4))
full_number = multiply_numbers(3, 6)
print(full_number)

#Question4
def shipping_message(order_total):
    if order_total >= 50:
        return "Free shipping"
    else:
        return "Shipping fee applies"

print(shipping_message(1))
print(shipping_message(86))

#Question5
def temperature_label(temperature_c):
    if temperature_c < 0:
        return "Frozen"
    #elif 0 >= temperature_c < 20:
    elif 0 <= temperature_c < 20:
        return "Cold"
    else:
        return "Warm"

print(temperature_label(-6))
print(temperature_label(19))
print(temperature_label(0))