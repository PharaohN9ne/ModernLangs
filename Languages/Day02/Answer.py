#Exercise 1
age = 73

if age >= 18:
    print("Adult")
else:
    print("Minor")

#Exercise2
password_length = 4

if password_length < 10:
    print("Password too short")
else:
    print("Password length okay")

#Exercise3
order_total = 99
is_member = False

if order_total >= 50 or is_member:
    print("Free shipping")
else:
    print("Shipping fee applies")

#Exercise4
temperature_c = -0

if temperature_c < 0:
    print("Frozen")
elif 0 <= temperature_c < 20:
    print("Cold")
else:
    print("Warm")

#Exercise5
role = "Admin"

if role.casefold() == "admin":
    print("Full access")
elif role.casefold() == "editor":
    print("Can edit content")
elif role.casefold() == "viewer":
    print("Read-only access")
else:
    print("Unknown role")