# CK, Loops Notes
import random

count = 1

while count <= 10:
    print(count)
    count += 1

ducks = 1
goose = random.randint(1,11)

while True:
    if ducks == goose:
        break
    print("Duck. . . .")
    ducks += 1 #ducks = ducks + 1
print("GOOSE!!!!")

# complex data type = holds other data in it
siblings = ["Levi", "Kamden", "Marissa", "Remi", "Chloe", "Andi", "Daisy"]
print(siblings[0])
# adding to a list
name = input("What is your name: ")
siblings.append(name) # <= adds the item to the end of the list
siblings.insert(3, "Caleb")
print(siblings)
# remove from a list
siblings.pop(3) # <= if no number given pop removes the last item
print(siblings)

# print each item in a list
for sibling in siblings:
    print(siblings)


# For loops
for num in range(1,25): # range builds a list for us (start point,end point)
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)