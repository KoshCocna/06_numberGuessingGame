from numGuessArt import logo
import random

print(logo)
print("Welcome the Number Guessing Game!\nI'm thinking a number between 1 and 100~")
num = random.randint(1,100)
level = input("Select your level pls, 'easy' or 'difficult': ")

if level == "easy":
    lives = 10
elif level == "difficult":
    lives = 5
else:
    lives = 0

while lives:
    print(f"You have {lives} attempts remaining to guess the number")
    guessedNum = int(input("Make a Guess: "))
    if guessedNum > num:
        print("Too high...")
        lives -= 1
    elif guessedNum < num:
        print("Too low...")
        lives -= 1
    else:
        print("You made it!")
        break
    if lives == 0:
        print(f"You lose... the guessed number was {num}")