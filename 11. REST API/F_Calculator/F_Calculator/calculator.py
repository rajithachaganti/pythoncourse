
from flask import (Flask, jsonify, request, abort, render_template)
import math

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add_args():
    print("------In add_args() method--------")
    if not request.json:  # {"argument1": 100, "argument2": 200}
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        try:
            arg1 = int(arg1)
            arg2 = int(arg2)
        except Exception:
            return jsonify({'answer': "Enter input as numbers"}), '400'
        answer = arg1 + arg2

        return jsonify({'answer': answer}), 200
    except KeyError:
        abort(400)

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
        except Exception:
            return jsonify({'answer': "Input not integers"}), '400'

        answer = arg1 * arg2
        return jsonify({'answer':answer}), 200
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


if __name__ == '__main__':
    app.run(debug=True)
