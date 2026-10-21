# CK, fixed ticket prices

while True:
    age = int(input("Enter your age: "))
    if age < 0:
        print ("That is not an age.\nPlease try again")
    else:
        break

matinee = input("Is this a matinee? (yes/no): ").lower()

if age < 5:
    price = 0
elif age < 13:
    price = 8
elif age < 65:
    price = 12
else:
    price = 9

if matinee == "yes":
    price = price - 3
if price == "-3":
    price == "0"

if price < 0:
    price = 0

print(f"Ticket price: ${price}")