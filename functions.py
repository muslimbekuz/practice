'''FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr vs Argument
(3) Keyword & Default arguments
(4) Scoupe
'''

print("==== DEFINE (parametr) vs CALL (argument) ====")
# build in function > print(), type()
# Function - reusable block of code
# Instead of block {} in Java, Python uses indentation

# Define - Parametr


def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# Call - Argument
result1 = greet('Tony')
print("result1:", result1)

result2 = greeting("Ali")
print("result2:", result2)

print("==== Keyword & Default arguments ====")
# DEFINE


def give_greet(name, age=20):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


# CALL
result3 = give_greet(name="Tony", age=23)
print("result3:", result3)

result4 = give_greet("Ali")
print("result4:", result4)


print("==== Scope ====")
b = 100  # 3

# DEFINE


def calculate(a, b):  # 2
    c = a*b  # 1
    print(f"the c value: {c}")


# CALL
calculate(5, 50)
