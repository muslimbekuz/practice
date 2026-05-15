# literal
nums = [1, 2, 3, 4, 5]

# contructor
letters = list("hello world")
print(letters)

fruits = ['apple', 'peach', 'banana', 'kiwi']
fruits[0] = 'melon'
print(fruits)

# tuple
animals = ('apple', True, 22, None)
print(animals[0])
# animals[0] = 'lion' -> ERROR

groups = ('mit', 'flexy', 'devex', 'mg')
a, b, *z = groups

print(a)
print(z)


print()


def sum(*args):
    total = 0
    for x in args:
        total += x
    print(total)


sum(1, 2, 3, 4)
sum(1, 2, 3)
sum(1, 2)

print()


def dic(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


dic(name='tony', age=23)
print()
dic(name='ali', ismarried=True)

print()


def greeting(*args, **kwargs):
    print("*args ->", args)
    print("**kwargs ->", kwargs)


greeting("hi", True, 22, name='Tony', age=23)

print()

tuple1 = [1, 2]
tuple2 = ('a', 'b', 'c')
zipped = zip(tuple1, tuple2)
print(list(zipped))
