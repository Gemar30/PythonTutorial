# Day 7 Hangman Project Step by Step

# How to break the complex problem

# hangman game

# STEP 1
import random
import hangman_art # or from hangman_art import logo, stages
import hangman_words #or from hangman_words import word_list


end_of_game = False
chosen_word = random.choice(hangman_words.word_list) # picking the word from word_list
word_length = len(chosen_word)
lives = 6

print(hangman_art.logo)
display = []

for _ in range(word_length):
    display += "_"
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter} \n Guest letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -=1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(display)}")   

    if "_" not in display:
        end_of_game = True
        print("You win")


    print(hangman_art.stages[lives])

