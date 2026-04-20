import random

def play_game():
    print("Welcome to the Number Guessing Game!")

    number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low! ")
        else:
            guessed_correctly = True
            print(f"Correct! You guessed it in {attempts} attempts.")

play_game()