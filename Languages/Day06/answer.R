#question 1

name <- "bob"
age <- 86
build_web_apps <- FALSE

cat (name, age, build_web_apps, "\n")

#question 2

password_length <- 33

if(password_length < 8){
  print("Password too short")
}
else {
  print("Password length okay")
}

#question 3

tasks <- c("make a movie", "wash the car", "pick up laundry")

for (x in tasks){
  print(x)
}

#question 4

add_tax <- function (price, tax_rate){
  return (price + (price * tax_rate))
}

finalPrice <- add_tax(88, .06)

print (finalPrice)

#question 5

status <- "outside"

show_status <- function(){
  status <- "inside"
  print(status)
}

show_status()
print(status)