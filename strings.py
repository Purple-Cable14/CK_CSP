# CK, String Notes

# string => anything inside of quotation marks. " " ' '

name = input('What is your name: ').strip().lower().capitalize()

age = input('how old are you: ')
print(type (age))

# Concatenation => puts two strings directly next to each other
print(age+age)

print(name + " " + "King")

#
sentence = "It was like a cloudless bunny."

print(sentence)
print(sentence.replace("bunny", "storm"))
print(len(name)) #<= gets the length of a string
print(f"Your name is {name}, that is {len(name)} letters long. Your first initial is {name[0]} I think I will call you {name[0:3]}")