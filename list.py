fruits = ['apple', 'banana', 'kiwi', 'cherry']

new_fruits = fruits[0:2]
print(new_fruits)
print(fruits[::2])
print(fruits[::-1])


print("list methods")
# append(), insert(), pop(), remove(), clear(), sort(), index()

numbers = [2, 3, 4]

numbers.append(5)
print(numbers)
numbers.insert(0, 1)
print(numbers)
numbers.pop()
print(numbers)
numbers.remove(3)
print(numbers)
del numbers[0:2]
print(numbers)
print(numbers.index(4))  # immutable
numbers.clear()
print(numbers)


nums = [4, 2, 1, 5, 3]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)


numbs = [5, 2, 12, 61]
new_numbs = sorted(numbs)  # immutable
print(numbs)
print(new_numbs)


print("lambda function")
def calculate(a, b): return a+b


print(calculate(1, 2))

print()

people = [
    ('tony', 23),
    ('fred', 19),
    ('ali', 17),
    ('john', 26)
]

people.sort(key=lambda person: person[1])
print(people)

people.sort(key=lambda person: person[0])
print(people)

print()

animals = ['dog', 'fish', 'dog']

for index, value in enumerate(animals):
    print(index, value)

print()

cars = [
    ('ferrari', 78),
    ('toyota', 87),
    ('audi', 116),
    ('bmw', 109),
    ('pagani', 33)
]

result = map(lambda car: car[0], cars)
print(list(result))
print()

result = filter(lambda car: car[1] > 50, cars)
print(list(result))
