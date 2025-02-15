#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# this route works
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# the rest of the routes do not work on view
@app.route('/print/<string:route>')
def print_string(route):
    print(route)
    return route

@app.route('/count/<int:num>')
def count(num):
    count = f''
    for n in range(num):
        count += f'{n}\n'
    return count

@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, num2, operation):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    
    return "Operation not supported. Please use one of the following operations: + - * div %"

if __name__ == '__main__':
    app.run(port=5555, debug=True)