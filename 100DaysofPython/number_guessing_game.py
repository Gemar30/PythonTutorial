# Day 12 Project
# Numebr Guessing Game
import random
from guess_number_art import logo
EASY_LEVEL = 10
HARD_LEVEL =  5 


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


def set_difficulty():
    
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print(logo)
    print("Welcome to the Number Guessing Game! ")
    print("I'm thinking of a number between 1 to 100.")

    # choose = input("Choose a difficulty. Type 'easy' or 'hard': ")
    # Choosing a random number between 1 -100

    answer = random.randint(1, 101)
    print(f"the correct answer is {answer}")

    # Make function to set difficulty (easy and difficult)

    # Let the user guess a number
    turns = set_difficulty()
   

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts to guess the number.")


        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of gasses, You lose!")
            return
        elif guess != answer:
            print("Guess again")

game()







    



# make a guess
# Too High or Too Lowa
# Guess again
# You have {number} attempts remaining to guess the number



# Easy = 10 attempts remaining
# Hard =  5 attempts remaining

