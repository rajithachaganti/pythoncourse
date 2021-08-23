

from flask import (Flask, jsonify, request, abort, render_template)
import math

app = Flask(__name__)


@app.route('/')
def index_page():
    print("Sending home page to customer")
    return render_template('index.html')

@app.route('/add_squares', methods=['POST'])
def add_sq_args():
    if not request.json:  # {"argument1": 100, "argument2": 200}
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        try:
            arg1 = int(arg1)
            arg2 = int(arg2)
        except Exception:
            return jsonify({'data': "Enter input as numbers"}), '400'
        result = arg1*arg1 + arg2*arg2
        return jsonify({'data': str(result),'status':'success'}), 200
        #return jsonify([result]), 200
    except KeyError:
        abort(400)

@app.route('/add', methods=['POST'])
def add_args():
    print("------Adding two arguments------")
    if not request.json:
        abort(400)
    print("Hello world")
    try:
        num1 = request.json['argument1']
        num2 = request.json['argument2']
        print("Data from UI :",num1,num2)
        try:
            n1 = int(num1)
            n2 = int(num2)
        except Exception:
            return jsonify({'answer': "Enter input as numbers"}), '400'
        add_res = n1 + n2

        return jsonify({'answer': add_res}), 200
    except KeyError:
        abort(400)



@app.route('/subtract', methods=['POST'])
def subtract_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        try:
            arg1 = int(arg1)
            arg2 = int(arg2)
        except Exception:
            return jsonify({'answer': "Input not integers"}), '400'
        answer = arg1 - arg2
        return jsonify({'answer':answer}), 200
    except KeyError:
        abort(400)


@app.route('/multiply', methods=['POST'])
def multiply_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        try:
            arg1 = int(arg1)
            arg2 = int(arg2)
            print("Received data from UI : ",arg1,arg2)
        except Exception:
            return jsonify({'answer': "Input is not integers"}), '400'

        answer = arg1 * arg2
        return jsonify({'answer':answer}), 202
    except KeyError:
        abort(400)


@app.route('/divide', methods=['POST'])
def divide_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        try:
            arg1 = int(arg1)
            arg2 = int(arg2)
        except Exception:
            return jsonify({'answer': "Input not integers"}), '400'
        answer = arg1 / arg2
        return jsonify({'answer':answer}), 200
    except KeyError:
        abort(400)
    except ZeroDivisionError:
        abort(400)


@app.route('/mod', methods=['POST'])
def mod_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        try:
            arg1 = int(arg1)
            arg2 = int(arg2)
        except Exception:
            return jsonify({'answer': "Input not integers"}), '400'

        answer = arg1 % arg2
        return jsonify({'answer':answer}), 200
    except KeyError:
        abort(400)
    except ZeroDivisionError:
        abort(400)


@app.route('/exp', methods=['POST'])
def exponent_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        try:
            arg1 = int(arg1)
            arg2 = int(arg2)
        except Exception:
            return jsonify({'answer': "Input not integers"}), '400'
        answer = arg1 ** arg2
        return jsonify({'answer':answer}), 200
    except KeyError:
        abort(400)


@app.route('/average', methods=['POST'])
def average_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        try:
            arg1 = int(arg1)
            arg2 = int(arg2)
        except Exception:
            return jsonify({'answer': "Input not integers"}), '400'

        answer = (float(arg1) + float(arg2)) / 2
        return jsonify({'answer':answer}), 200
    except KeyError:
        abort(400)


@app.route('/log', methods=['POST'])
def log_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        try:
            arg1 = int(arg1)
            arg2 = int(arg2)
        except Exception:
            return jsonify({'answer': "Input not integers"}), '400'
        answer = math.log(arg1, arg2)

        return jsonify({'answer':answer}), 200
    except KeyError:
        abort(400)
    except ZeroDivisionError:
        # occurs when you try a log(a,1)
        abort(400)
    except ValueError:
        # occurs when you try a log(a,0)
        abort(400)

def pow_of_vals():
    pass


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    # app.run()
    # app.run(host='localhost', port=4000)
    # app.run(debug=True)
    # app.run(port = '4050', debug=True)