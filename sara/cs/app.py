from flask import Flask, render_template, request

app = Flask(__name__)

# you need to Captaliz the word so it can work😉
REG = {}

MOOOD = [
    " Nice 😏 ",
    " Cool 🤓 ",
    " Awesome! 😍 "
]


@app.route("/")
def index():
    return render_template("index.html", moood=MOOOD)
# you need to write the "app.route", "return" the same name to make it run😉


@app.route("/don", methods=["POST"])
def don():
    name = request.form.get("name")
    mod = request.form.get("mod")
    REG[name] = mod
    return render_template("don.html")


@app.route("/mood")
# Def need to be MOD so it can run the code // mod = request.form.get("mod") // be cearfull for this tiney mistakes😉
def mood():
    return render_template("mood.html", mood=REG)


# This pice of code is needed to run the code😉
if __name__ == "__main__":
    app.run()
    
#sport = mod
#sports = moood
#html = mood