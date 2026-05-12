#question 1
from oauthlib.uri_validate import authority

favorite_foods = ['apple', 'papaya', 'dragonfruit']

print(favorite_foods)
print(favorite_foods[0])
print(favorite_foods[2])
favorite_foods.append('grapes')
print(len(favorite_foods))

#question 2

user_profile = ('bob', 36, True)
print(user_profile)

#question 3

book = {
    "title": "bobbie did it again",
    "author": "ron johnson",
    "pages": 465,
}
print(book)
print(book['title'])

#question 4

skills = {"boxing", "Muay Thai", "karate", "kickboxing", "Muay Thai"}
print(skills)
print("MMA" in skills)

#question 5

student = {
    "name" : "bobby",
    "languages" : ["English", "Spanish", "British English"],
    "active" : True
}
print(student)
print(student.get('languages'))