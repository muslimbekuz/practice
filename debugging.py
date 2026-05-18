''' Package & Debugging
(1) Python Package & Core Package
(2) Package Manager & External Package
(3) Debugging
'''


import turtle
print("==== Python Package & Core Package ===== ")
''' Python Package/Modules: Core, File and External
'''
# Core Packages > https://docs.python.org/3/libary


# Core Packages
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)
t.circle(100)

turtle.done()

print("---------")
my_file = open("material/message.txt")
try:
    content = my_file.read()
    print("content:", content)

finally:
    my_file.close()

# with - Context Manager
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)
print("Done")
