import turtle, time, random
print(f"Hello")
name = input("What is your name?\n").capitalize()
print(f"Hello {name}! Nice to meet you!")
print("Let's play a game!")
gameplay = True
while gameplay: 
    randnumber = random.randint(1,10)
    number = 0
    while 1 > number or number > 10:
        number = int(input("Enter a number from 1-10:\n"))
        if 1 <= number <= 10:
            pass
        else: print("Your number is too large/small! Please redo that number!")
    print(f"Your number is {number} and the actual number was {randnumber}!")
    if randnumber == number:
        print("You got the exact nummber!")
    elif randnumber > number:
        print("Oof! You were a bit too low in your number choice!")
    else:
        print("Oof! You were a bit too high in your selection!")
    gameplay = input("Do you want to play again? Type Yes to Play Again. \n").lower()
    if gameplay == ('yes'):
        gameplay = True
    else:
        print("Goodbye!")
        gameplay = False
