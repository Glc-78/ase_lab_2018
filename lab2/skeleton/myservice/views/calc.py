from flakon import JsonBlueprint
from flask import Flask, request, jsonify

calc = JsonBlueprint('calc', __name__)

@calc.route('/calc/sum', methods=['GET'])
def sum():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    result = m
    if n < 0:
        for i in range(abs(n)):
            result -= 1
    else:
        for i in range(n):
            result += 1
    return jsonify({'result: ': str(result)})


@calc.route('/calc/div', methods=['GET'])
def divide(m, n):
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    result = 0
    sign = 1
    if n == 0:
        raise ZeroDivisionError("You cannot divide by 0!")
    if (n < 0 and m > 0) or (n > 0 and m <0):
        sign = -1
    n = abs(n)
    m = abs(m)
    while m-n >= 0:
        m -= n
        result += 1
    return jsonify({'result: ': str(sign * result)})

@calc.route('/calc/sub', methods=['GET'])
def subtract(m, n):
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    result = m
    if n < 0:
        for i in range(abs(n)):
            result += 1
    else:
        for i in range(abs(n)):
            result -= 1
    return jsonify({'result: ': str(result)})

@calc.route('/calc/mul', methods=['GET'])
def multiply(m, n):
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    sign = 1
    if n == 0 or m == 0:
        return 0
    if (m > 0 and n < 0) or (m < 0 and n > 0):
        sign = -1
    result = m = abs(m)
    n = abs(n)
    for i in range(n-1):
        result += m
    return jsonify({'result: ': str(sign * result)})

