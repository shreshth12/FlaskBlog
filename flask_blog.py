from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '04106331e37053a7'
data = [
    {'Name' : 'Shreshth',
    'age' : 21,
    'content' : 'Do not give up',
    'weight' : 'I won\'t tell you',
    'date_posted' : '29th July',
    },

    {'Name' : 'Sarthak',
    'age' : 16,
    'content' : 'Do not give up when your in US',
    'weight' : 'I won\'t tell you',
    'date_posted' : '29th July',
    }
]

@app.route("/")
@app.route("/home")
def homePage():
    return render_template("home.html", post = data, title = 'HOMEPAGE')

@app.route("/about")
def about():
    return render_template("about.html", title = 'ABOUTPAGE')

@app.route("/register")
def register():
    form = RegistrationForm()

    return render_template("register.html", title = 'REGISTRATION PAGE', form = form)

@app.route("/login")
def login():
    form = LoginForm()

    return render_template("login.html", title = 'LOGIN PAGE', form = form)

if __name__ == "__main__":
    app.run(debug=True)