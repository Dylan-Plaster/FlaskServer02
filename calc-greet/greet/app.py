from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return ('Hello World')

@app.route('/welcome')
def welcome():
    return 'welcome'

@app.route('/welcome/back')
def welcomeBack():
    return 'welcome back'

@app.route('/welcome/home')
def welcomeHome():
    return 'welcome home'