print("WELCOME TO PYTHON ADVENTURE!")

name = input("Enter your name: ")

print("Hello", name)
print("Your adventure begins now!")

score = 0

answer = input("Do you want to enter the mystery forest? yes/no: ")

if answer.lower() == "yes":
    print("You found a treasure!")
    score += 10
else:
    print("You missed the treasure!")

print("Your score:", score)
