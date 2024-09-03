from flask import Flask, render_template
from config import SECRET_KEY, SQLALCHEMY_DATABASE_URI, DEBUG

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["DEBUG"] = DEBUG

@app.route("/")
def say_hi():
    return render_template("index.html", say_hi="Hello World")

if __name__ == "__main__":
    app.run()