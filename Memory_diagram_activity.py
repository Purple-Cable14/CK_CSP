while True:
    user_input = input("How many Fibonacci numbers do you want? Enter a whole number from 1 to 20: ")

    try:
        count = int(user_input)
    except ValueError:
        print("You need to type a whole number.")
        continue

    if count < 1 or count > 10000:
        print("Please stay in the range of 1 to 20.")
        continue

    break

sequence = []
a, b = 0, 1

for _ in range(count):
    sequence.append(a)
    a, b = b, a + b

print(*sequence)