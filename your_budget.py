# CK, Your Budget

while True:
    try:
        income=float(input("What is your monthly income: $"))
        break
    except:
        print("That is not a number.")

while True:
    try:
        rent=float(input("What is your monthly rent/mortgage: $"))
        break
    except:
        print("That is not a number.")

while True:
    try:
        utilities=float(input("What is your monthly utilities: $"))
        break
    except:
        print("That is not a number.")

while True:
    try:
        groceries=float(input("What is your monthly groceries: $"))
        break
    except:
        print("That is not a number.")

while True:
    try:
        transportation=float(input("What is your monthly transportation: $"))
        break
    except:
        print("That is not a number.")

print(f"your rent is {rent/income*100}% of your income")

print(f"your utilities is {utilities/income*100}% of your income")

print(f"your groceries is {groceries/income*100}% of your income")

print(f"your transportation is {transportation/income*100}% of your income")

print(f"This is your spending money for the month: ${income-rent-utilities-groceries-transportation}")