# CK, Fixing user inputs

while True:
    color = input("Tell me a color that is only one word: ").strip().capitalize()
    if color.isnumeric():
        print("That is a number not a color!")
    elif " " in color:
        print("I said one color!")
    else:
        break

print(f"We painted the walls {color}!")