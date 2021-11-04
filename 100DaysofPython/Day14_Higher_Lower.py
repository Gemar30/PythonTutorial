# Day 15 Project
from higher_lower_art import logo, vs
from game_data import data
from screen_clear import clear
import random


""" Format the account data into printable format"""

def format_data(account):

    account_name = account["name"] # Key
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Takes the user account and followers counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

 
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data) # pick one random account
# Make the game repeatable
while game_should_continue:

    # Generate a random account from game data.

    # Making the account at position B become the next account at Position A.
    account_a = account_b 
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Againsts B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A', or 'B': ").lower()

    ## Get follower count of each account

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
    # Clear the screen
    clear()
    print(logo)



    # Score keeping
    if is_correct:
        score += 1 
        print(f"You're right, Current Score: {score} ")
    else:
        game_should_continue = False
        print(f"Sorry, That's Wrong! Final Score: {score}")







