from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    return redirect(url_for("home"))


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        user = request.form['nm']
        return render_template("submit.html", u=user)
    else:
        user = request.args.get('nm')
        return render_template("submit.html", u=user)


if __name__ == "__main__":
    app.run()
