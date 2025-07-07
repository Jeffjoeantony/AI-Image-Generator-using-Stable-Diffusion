from flask import Flask, render_template,request

app = Flask(__name__)

# name = "Jeff"

# @app.route('/')
# def home():
#     return render_template('index.html',name="Jeff")

# app.run()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username,password)
    if username == "jeff" and password == "jeff":
        return render_template('home.html',user=username)
    elif username == "megha" and password == "megha":
        return render_template('home.html',user=username)
    elif username == "anna" and password == "anna":
        return render_template('home.html',user=username)
    else:
        return "Login Failed"

app.run()