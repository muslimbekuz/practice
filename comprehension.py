''' Comprehension
(1) What is Comprehension & list comp.
(2) set and dictionary comp.
'''

print("==== What is Comprehension & list comp. ==== ")
# Comprehension acts like spread operators!

''' Comprehension general syntax:
    a) *iterable
    b) <expression> for item in iterable
    c) <expression> for item in iterable <condition>
'''

# list comp.

numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]  # a version

print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

print("---------")
people = [("Tony", 23), ("Ali", 19), ("John", 25)]
list_people = [person[0] for person in people]  # b version
print("list_people", list_people)

cars = [
    ('Ferrari', 78),
    ('Toyota', 87),
    ('Audi', 116),
    ('Bmw', 109),
    ('Pagani', 33)
]

list_cars = [car[0] for car in cars if car[1] > 80]  # c version
print("list_cars:", list_cars)
