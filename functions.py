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
