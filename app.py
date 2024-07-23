from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")

def landing():
    return render_template('index.html')

@app.route("/signin")
def signin():
    return "this will be our sign in page"


if __name__ == "__main__":
    app.run(debug=True, port=8080)
