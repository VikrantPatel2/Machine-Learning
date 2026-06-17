from flask import Flask
'''
It creates an instance of the flask class , which will be your WSGI(Web Server Gateway Interface) application.
'''
app=Flask(__name__)


@app.route('/')
def wilecome():
    return "Welcome to  best Flask course. This should be an amazing course."

@app.route('/index')
def index():
    return "This is the index page."


if __name__=="__main__":
    app.run(debug=True)