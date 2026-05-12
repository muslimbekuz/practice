''' CLASS
(1) What is class
(2) ordinary vs static properties
(3) special methods
'''

print("==== What is class ====")
# class - blueprint for object creation!
# stucture > state | constuctor | method


class Person():
    # state
    message = "static state property"
    # constuctor

    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass
    # method

    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says: I am {self.age} years old!")

    @classmethod
    def explain(cls):
        print("static method property executed!")


person1 = Person("Tony", 23)
person2 = Person("Ali", 20)
person3 = Person("Martin", 35)

# ordinary state
name = person1.name
print("person1.name:", person1.name)

# ordinary method
person1.introduce()
person2.say_age()

print("==== ordinary vs static properties ====")
# static state
new_message = Person.message
print("new_message:", new_message)

# static method
Person.explain()
