import random

secret_number = random.randint(1, 10)

guess = 0

while guess != secret_number:
    guess = int(input("Guess a number (1-10): "))

    if guess == secret_number:
        print("Congratulations! You guessed it correctly. 🎉")
    else:
        print("Wrong! Try Again.")
