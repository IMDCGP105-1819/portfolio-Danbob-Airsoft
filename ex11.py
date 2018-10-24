from random import *
Number = randint(1,30)
Guess = 0
while Guess != Number:
    Guess = int(input("Please enter your guess between 1 and 30 "))
    if Guess == Number:
        print("Correct")
    elif Guess > Number:
        print("Too high, please guess again")
    elif Guess < Number:
        print("Too low, please guess again")
