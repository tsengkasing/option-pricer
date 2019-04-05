#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from flask import Flask, request, make_response, send_file
from black_scholes import black_scholes
from closed_form_formulas import \
    geom_asian_call_option, \
    geom_asian_put_option, \
    geom_basket_call_option, \
    geom_basket_put_option
from MC import \
    Arith_Call_Basket, \
    Arith_Call_Option, \
    Arith_Put_Basket, \
    Arith_Put_Option

# Create App
app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/')
def index():
    return


@app.route('/api/european_option/<option_type>', methods=['GET'])
def european_call_option(option_type):
    """European Option

    test using
    `curl http://localhost:3721/api/european_option/call?S=100&K=100&T=0.5&sigma=0.2&r=0.01&q=0.5`

    :param option_type: string
    :return: response
    """
    S = request.args.get('S', type=float)
    sigma = request.args.get('sigma', type=float)
    r = request.args.get('r', type=float)
    q = request.args.get('q', type=float)
    T = request.args.get('T', type=float)
    K = request.args.get('K', type=float)
    try:
        option_value = black_scholes(option_type, S, K, T, sigma, r, q)
    except Exception as error:
        return response_json(1, str(error), None)
    return response_json(0, 'OK', option_value)


@app.route('/api/geometric_asian_option/<option_type>', methods=['GET'])
def geometric_asian_option(option_type):
    """Geometric Asian option

    :param option_type: string
    :return: response
    """
    S = request.args.get('S', type=float)
    sigma = request.args.get('sigma', type=float)
    r = request.args.get('r', type=float)
    T = request.args.get('T', type=float)
    K = request.args.get('K', type=float)
    n = request.args.get('n', type=int)
    if option_type == 'call':
        option_value = geom_asian_call_option(S, sigma, r, T, K, n, t=0)
    elif option_type == 'put':
        option_value = geom_asian_put_option(S, sigma, r, T, K, n, t=0)
    else:
        return response_json(1, 'Error Option Type', None)
    return response_json(0, 'OK', option_value)


@app.route('/api/arithmetic_asian_option/<option_type>', methods=['GET'])
def arithmetic_asian_option(option_type):
    """Arithmetic Asian option

    :param option_type: string
    :return: response
    """
    S = request.args.get('S', type=float)
    sigma = request.args.get('sigma', type=float)
    r = request.args.get('r', type=float)
    T = request.args.get('T', type=float)
    K = request.args.get('K', type=float)
    n = request.args.get('n', type=int)
    m = request.args.get('m', type=int)
    control = request.args.get('control', type=int) == 1  # True | False
    seed = request.args.get('seed', type=int)
    if option_type == 'call':
        option_value = Arith_Call_Option(S, sigma, r, T, K, n, m, control, seed)
    elif option_type == 'put':
        option_value = Arith_Put_Option(S, sigma, r, T, K, n, m, control, seed)
    else:
        return response_json(1, 'Error Option Type', None)
    return response_json(0, 'OK', option_value)


@app.route('/api/geometric_basket_option/<option_type>', methods=['GET'])
def geometric_basket_option(option_type):
    """Geometric basket option

    :param option_type: string
    :return: response
    """
    S_1 = request.args.get('S1', type=float)
    S_2 = request.args.get('S2', type=float)
    sigma_1 = request.args.get('sigma1', type=float)
    sigma_2 = request.args.get('sigma2', type=float)
    r = request.args.get('r', type=float)
    T = request.args.get('T', type=float)
    K = request.args.get('K', type=float)
    rho = request.args.get('rho', type=float)

    if option_type == 'call':
        option_value = geom_basket_call_option(S_1, S_2, sigma_1, sigma_2, r, T, K, rho, t=0)
    elif option_type == 'put':
        option_value = geom_basket_put_option(S_1, S_2, sigma_1, sigma_2, r, T, K, rho, t=0)
    else:
        return response_json(1, 'Error Option Type', None)
    return response_json(0, 'OK', option_value)


@app.route('/api/arithmetic_basket_option/<option_type>', methods=['GET'])
def arithmetic_basket_option(option_type):
    """Arithmetic basket option

    :param option_type: string
    :return: response
    """
    S_1 = request.args.get('S1', type=float)
    S_2 = request.args.get('S2', type=float)
    sigma_1 = request.args.get('sigma1', type=float)
    sigma_2 = request.args.get('sigma2', type=float)
    r = request.args.get('r', type=float)
    T = request.args.get('T', type=float)
    K = request.args.get('K', type=float)
    rho = request.args.get('rho', type=float)
    m = request.args.get('m', type=int)
    control = request.args.get('control', type=int) == 1  # True | False
    seed = request.args.get('seed', type=int)
    if option_type == 'call':
        option_value = Arith_Call_Basket(S_1, S_2, sigma_1, sigma_2, r, T, K, rho, m, control, seed)
    elif option_type == 'put':
        option_value = Arith_Put_Basket(S_1, S_2, sigma_1, sigma_2, r, T, K, rho, m, control, seed)
    else:
        return response_json(1, 'Error Option Type', None)
    return response_json(0, 'OK', option_value)


def response_json(status, msg, data):
    """create json format response

    :param status: int, status code, 0 for OK, 1 for error
    :param msg: string, message
    :param data: any
    :return: dict
    """
    response = make_response(json.dumps({
        'status': status,
        'msg': msg,
        'data': data
    }))
    response.headers['Content-Type'] = 'application/json; Charset=utf8'
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3721, debug=True)
