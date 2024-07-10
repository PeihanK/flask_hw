from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, Flask!'


@app.route('/user/<name>')
def user(name):
    return f'Welcome, {name}!'


@app.route('/double/<int:number>')
def double_number(number):
    return f'{number} doubled is {number * 2}'


@app.route('/square/<float:number>')
def square_number(number):
    return f'The square of {number} is {number * number}'


@app.route('/reverse/<path:text>')
def reverse_text(text):
    return f'{text} reversed is {text[::-1]}'


if __name__ == '__main__':
    app.run(debug=True)
