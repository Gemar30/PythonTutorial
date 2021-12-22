from flask import Flask
import random

app = Flask(__name__)

# Generate a random number as answer
answer = random.randint(0, 9)


# The website starts with a main page
@app.route("/")
def higher_lower_game():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/xT0xeuOy2Fcl9vDGiA/giphy.gif'>"


# take user input and generate a webpage base on the number
@app.route("/<int:number>")
def user_guess(number):
    if number > answer:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/UVsEApdS35zdJitRBd/giphy.gif' width=500>"
    elif number < answer:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/PR3585ZZSvcHO9pa76/giphy.gif' width=500>"
    elif number == answer:
        return "<h1 style='color: #198964'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/12MY94aT1qTFjW/giphy.gif' width=500>"
    else:
        return "<h1>Please guess a number between 0 and 9, try again :)</h1>" \
               "<img src='https://media.giphy.com/media/xT0xeuOy2Fcl9vDGiA/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)