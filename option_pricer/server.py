#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from math import isnan
from flask import Flask, request, make_response
from black_scholes import black_scholes
from implied_volatility import calc_implied_volatility
from binomial_tree import american_call_binomial_tree, american_put_binomial_tree
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
@app.route('/index')
def index():
    return app.send_static_file('index.html')


@app.route('/api/european_option/<option_type>', methods=['GET'])
def european_option(option_type):
    """European Option

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


@app.route('/api/implied_volatility/<option_type>', methods=['GET'])
def implied_volatility(option_type):
    """Implied Volatility

    :param option_type: string
    :return: response
    """
    S = request.args.get('S', type=float)
    r = request.args.get('r', type=float)
    q = request.args.get('q', type=float)
    T = request.args.get('T', type=float)
    K = request.args.get('K', type=float)
    option_premium = request.args.get('optionPremium', type=float)
    try:
        option_value = calc_implied_volatility(option_type, S, K, T, r, option_premium, q)
    except Exception as error:
        return response_json(1, str(error), None)
    return response_json(0, 'OK', option_value)


@app.route('/api/american_option/<option_type>', methods=['GET'])
def american_option(option_type):
    """American Option

    :param option_type: string
    :return: response
    """
    S = request.args.get('S', type=float)
    sigma = request.args.get('sigma', type=float)
    r = request.args.get('r', type=float)
    T = request.args.get('T', type=float)
    K = request.args.get('K', type=float)
    N = request.args.get('N', type=float)
    if option_type == 'call':
        option_value = american_call_binomial_tree(S, sigma, r, T, K, N)
    elif option_type == 'put':
        option_value = american_put_binomial_tree(S, sigma, r, T, K, N)
    else:
        return response_json(1, 'Error Option Type', None)
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
        option_value1, option_value2 = Arith_Call_Option(S, sigma, r, T, K, n, m, control, seed)
    elif option_type == 'put':
        option_value1, option_value2 = Arith_Put_Option(S, sigma, r, T, K, n, m, control, seed)
    else:
        return response_json(1, 'Error Option Type', None)
    if isnan(option_value1):
        option_value1 = 'NaN'
    if isnan(option_value2):
        option_value2 = 'NaN'
    return response_json(0, 'OK', [option_value1, option_value2])


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
    try:
        import webbrowser, threading
        threading.Timer(1.25, lambda: webbrowser.open('http://localhost:3721')).start()
    except:
        print('Fail to open browser automatically.')
    print('Please Open Browser and visit http://localhost:3721')
    app.run(host='0.0.0.0', port=3721)
