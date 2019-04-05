#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scipy.stats as si
from math import sqrt, log, e
from black_scholes import black_scholes


def calc_implied_volatility(option_type, S0, K, T, r, V_true, q):
    sigmahat = sqrt(2 * abs((log(S0 / K) + (r - q) * T) / T))
    tol = 1e-8
    sigma = sigmahat
    sigmadiff = 1
    n = 1
    n_max = 100
    while sigmadiff >= tol and n < n_max:
        V = price(option_type, S0, K, T, sigma, r, q)
        vega = vega_call(S0, K, r, sigma, T, q)
        if vega == 0.0:
             return 'NaN'
        increment = (V - V_true) / vega
        sigma -= increment
        n += 1
        sigmadiff = abs(increment)
    if n >= n_max and sigmadiff >= tol:
        return 'NaN'
    return sigma


def price(option_type, S, K, T, sigma, r, q):
    """Option Value

    Args:
        option_type: str, 'call' | 'put'
    """
    return black_scholes(option_type, S, K, T, sigma, r, q)


def vega_call(S, K, r, sigma, T, q):
    d1 = (log(S / K) + (r - q) * T) / (sigma * sqrt(T)) + 0.5 * sigma * sqrt(T)
    return S * (e ** (-q * T)) * sqrt(T) * si.norm.pdf(d1, 0.0, 1.0)


if __name__ == '__main__':
    sigma = calc_implied_volatility(option_type='call', S0=100, K=100, T=1.0, r=0.01, V_true=1, q=1)
    print(sigma)
