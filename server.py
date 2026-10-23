from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(1, 20)
print(f"(Psst... the number is {random_number})")


@app.route("/")
def home():
    return ('<h1>Guess a number between 1 and 20</h1>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bjh2NHhldDllMTIyaGRib3hrNDZjaGdhdDRoNTc3NGcyZmM3YmRmMCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l0IynWug8KMW0sBeE/giphy.gif">')


@app.route("/<int:guess>")
def check_guess(guess):
    if guess < random_number:
        return ('<h1 style="color: red">Too low, try again!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    elif guess > random_number:
        return ('<h1 style="color: purple">Too high, try again!</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    else:
        return ('<h1 style="color: green">You found me!</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')


if __name__ == "__main__":
    app.run(debug=True)
