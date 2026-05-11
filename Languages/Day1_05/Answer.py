#Question1
def show_city():
    city = "Bowie"
    print(city)

show_city()

#Question2
course_name = "hello"
def print_course():
    print(course_name)

print_course()

#Question3
status = "outside"
def show_status():
    status = "inside"
    print(status)

show_status()
print(status)

#Question4
def add_tax(price, tax_rate):
    #return price + tax_rate
    return price + (price * tax_rate)

final_price = add_tax(100, .06)
print(final_price)

#Question5
def outer_message():
    message = "hello"
    def inner_message():
        print(message)
    inner_message()
outer_message()