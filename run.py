# Dunder __builtins__, __init__
message = "Hello world!"
print(message)

result = type(message)
print("result:", result)

''' in python, there are builtin tools:
(1) TYPES > int float str list dict
(2) FUNCTION > print() len() input() type()
(#) CONSTANS > True False None
'''

print(dir(__builtins__))
