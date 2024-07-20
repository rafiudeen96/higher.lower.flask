import random

from flask import Flask,redirect,url_for

app = Flask(__name__)

correct_number = 0
total_guess = 2

@app.route("/")
def home():
    global correct_number
    global total_guess
    total_guess = 2
    correct_number = random.randint(0,9)
    print(correct_number)
    return "<h1> Guess a number between 0 and 9 </h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:user_guess>")
def guess(user_guess):
    global total_guess
    if user_guess == correct_number:
        return "<h1 style='color:green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='correct'>"
    else:
        if total_guess == 1:
            return redirect(url_for('home'))
        else:
            if user_guess < correct_number:
                total_guess-=1
                return "<h1 style='color:red'>Too Low, Try again!</h1>" \
                       "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='Low'>" \
                       f"<h2>{total_guess} Try left </h2>"

            else:
                total_guess-=1
                return "<h1 style='color:violet'> Too High,Try again!</h1>" \
                       "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='High'>" \
                       f"<h2>{total_guess} Try left </h2>"

if __name__ == "__main__":
    app.run(debug=True)