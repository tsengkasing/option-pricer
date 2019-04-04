#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from flask import Flask, request
from option_pricer.european_option import black_scholes

# Create App
app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello'


@app.route('/european_option/<option_type>', methods=['GET', 'POST'])
def european_call_option(option_type):
    """European Option

    test using
    `curl http://localhost:3721/european_option/call?S=100&K=100&T=0.5&sigma=0.2&r=0.01&q=0.5`

    :param option_type: string
    :return: response
    """
    S = request.args.get('S', type=int)
    K = request.args.get('K', type=int)
    T = request.args.get('T', type=float)
    sigma = request.args.get('sigma', type=float)
    r = request.args.get('r', type=float)
    q = request.args.get('q', type=float)
    print(S, K, T, sigma, r, q)
    try:
        option_value = black_scholes(option_type, S, K, T, sigma, r, q)
    except Exception as error:
        return response_json(1, str(error), None)
    return response_json(0, 'OK', option_value)


def response_json(status, msg, data):
    """create json format response

    :param status: int, status code, 0 for OK, 1 for error
    :param msg: string, message
    :param data: any
    :return: dict
    """
    return json.dumps({
        'status': status,
        'msg': msg,
        'data': data
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3721, debug=True)
