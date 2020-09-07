# Put your app in here.
from flask import Flask, request
from operations import add, sub, div, mult

app = Flask(__name__)

ops = {
    'add': add,
    'sub': sub,
    'div': div,
    'mult': mult
}

### Better version here:
@app.route('/math/<operation>')
def handle(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    
    return str(ops[operation](a,b))

    








# @app.route('/add')
# def addition():
#     a = int(request.args['a'])
#     b = int(request.args['b'])
    
#     return str(add(a,b))




# @app.route('/sub')
# def subtraction():
#     a = int(request.args['a'])
#     b = int(request.args['b'])
    
#     return str(sub(a,b))





# @app.route('/mult')
# def multiplication():
#     a = int(request.args['a'])
#     b = int(request.args['b'])
    
#     return str(mult(a,b))




# @app.route('/div')
# def division():
#     a = int(request.args['a'])
#     b = int(request.args['b'])
    
#     return str(div(a,b))