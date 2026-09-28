# CK, Number Information

for number in range(1,21):
    if number % 2 == 0:
        if number % 5 == 0:
            print(f"{number} is even and is divisible by five.")
        else:
            print(f"{number} is even and is not divisible by five.")
    else:
        if number % 2 != 0:
            if number % 5 == 0:
                print(f"{number} is odd and is divisible by five.")
            else:
                print(f"{number} is odd and is not divisible by five.")