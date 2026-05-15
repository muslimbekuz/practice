
'''
    LOOP 
        1 - for
        2 - break/else
        3 - while
'''

text = "MIT"

for letter in text:
    print(letter)

nums = [1, 2, 3, 4, 5]
for n in nums:
    print(n)

car_obj = dict(name="porsche", year=2026, model='911')
for key in car_obj:
    print(key, car_obj[key])

for key, value in car_obj.items():
    print(key, value)

range_obj = range(5)
for n in range_obj:
    print(n)

for x in range(1, 20, 2):
    if x > 10:
        break
        print(x)
else:
    print("reached else")

print("==== while operator =====")
numb = 40
while numb > 0:

    numb -= 10
    print(f"the numb equals {numb}")

print("-----------")
count = 0
while True:
    count += 1
    x = int(input("Find number: "))
    if x == 41:
        print("You found the number in", count, "step")
        break
    else:
        print("Wrong, please try again")
