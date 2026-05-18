''' Package & Debugging
(1) Python Package & Core Package
(2) Package Manager & External Package
(3) Debugging
'''


from PIL import Image
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


print("==== Package Manager & External Package ===== ")
# External Package > https://pypi.org/
'''Package Managers:
    Python > pip
    NodeJS > npm yarn
    PHP > composer
    MacOS > brew
    '''
with Image.open("material/CR7.jpg") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("material/GOAT.png")


print("==== Debugging ===== ")


def get_summary(*args):  # Define
    total_ammount = 0
    for a in args:
        total_ammount += a
        return total_ammount  # solve the bug via debugging


test = 100
result = get_summary(1, 2, 3, 4, 5,)  # Call
print("result:", result)
