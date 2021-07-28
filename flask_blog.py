from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def homePage():
    return "<h1>This is my homepage</h1>"

@app.route("/about")
def about():
    return "<h1>This is my about page</h1>"

if __name__ == "__main__":
    app.run(debug=True)