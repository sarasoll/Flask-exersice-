from flask import Flask, render_template, request

app = Flask(__name__)

done = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    myname = request.form.get("myname")
    myvipe = request.form.get("myvipe")
    done[myname] = myvipe
    return render_template("register.html")

@app.route("/done")
def done():
    return render_template("done.html", done=done)


if __name__ == "__main__":
    app.run()