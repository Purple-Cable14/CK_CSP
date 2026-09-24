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