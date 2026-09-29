# CK, Functions Notes
# | helps with, makes it easier to read,
# V and breaks problem into smaller pieces
def stupid_proof(money):
    while True:
        try:
            amount = float(input(f"What is your monthly {money}: "))
            return amount
        except:
            print("That isn't a number XD")

# Write all your variables
income = stupid_proof("income")
rent = stupid_proof("rent")
utilities = stupid_proof("utilities")
groceries = stupid_proof("groceries")
transportation = stupid_proof("transportation")
saveings = income * .1

# Write any function you are using (define/def starts new function.) Then name your function. put parenthesis after the name. Then parameters. parameters=pieces of info needed for the variable to run/argument. End line with colon. Next line. Name function. "Return"
def calc_percent(income, bill):
    return round(bill/income *100)

# outputs for the user
print(f"Your rent is ${rent:.2f} that is {calc_percent(income,rent)} % of your income.")
print(f"Your utilities is ${utilities:.2f} that is {calc_percent(income,utilities)} % of your income.")
print(f"Your groceries is ${groceries:.2f} that is {calc_percent(income,groceries)} % of your income.")
print(f"Your transportation is ${transportation:.2f} that is {calc_percent(income,transportation)} % of your income.")
print(f"You should save ${saveings:.2f} that is {calc_percent(income,saveings)}% of your income.")
print(f"You have ${income-rent-utilities-groceries-transportation-saveings:.2f} left to spend!")