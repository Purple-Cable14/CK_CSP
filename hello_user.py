# CK, Hello User

while True:
    name = input("Hello User! What is your first name?: ").strip().capitalize()
    if name.isnumeric():
        print("Are you sure that is a name. It seems kinda weird, please try again.")
    elif " " in name:
        print("I'm sorry, but I asked for your first name.")
    else:
        break

print(f"Hello {name}! I would give you a handshake, but I don't have any arms. XD")