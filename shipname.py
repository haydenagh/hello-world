import random

print("Hello! Please enter your name and the name of the person you'd like to ship!\n")
name1 = input("What's your name? ")
name2 = input("Who is the other person? ")

# Generates either a 1 or a 2
aNumber = random.randrange(1, 3) 

# Changes the order of the names to make it more fun :)
if aNumber == 1:
    firstName = name1
    secName = name2
else:
    firstName = name2
    secName = name1

# First name goes from the first char to the middle char
firstName = firstName[0:int(len(firstName)/2)]
# Second name goes from the half char to the end char
secName = secName[int(len(secName)/2):]

print(f"Your ship name is: {firstName}{secName}")