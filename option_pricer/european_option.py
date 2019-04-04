#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import log, sqrt, e
import scipy.stats as si


def black_scholes(option_type, S, K, T, sigma, r, q):
    """Calculate Black-Scholes Formulas

    :param option_type: string, 'call' | 'put'.
    :param S: int, spot price.
    :param K: int, strike price.
    :param T: float, time to maturity, in year.
    :param sigma: float, volatility of underlying asset.
    :param r: float, risk-free interest rate.
    :param q: float, repo rate.

    Returns:
        values of either call and put options.
    """
    d1 = (log(S / K) + (r - q) * T) / (sigma * sqrt(T)) + 0.5 * sigma * sqrt(T)
    d2 = (log(S / K) + (r - q) * T) / (sigma * sqrt(T)) - 0.5 * sigma * sqrt(T)

    if option_type == 'call':
        return S * (e ** (-q * T)) * si.norm.cdf(d1, 0.0, 1.0) - K * (e ** (-r * T)) * si.norm.cdf(d2, 0.0, 1.0)
    elif option_type == 'put':
        return K * (e ** (-r * T)) * si.norm.cdf(-d2, 0.0, 1.0) - S * (e ** (-q * T)) * si.norm.cdf(-d1, 0.0, 1.0)
    else:
        raise Exception('Error Option Type')


# For testing
if __name__ == '__main__':
    call_option = black_scholes(option_type='call', S=100, K=100, T=0.5, sigma=0.2, r=0.01, q=0.2)
    put_option = black_scholes(option_type='put', S=100, K=100, T=0.5, sigma=0.2, r=0.01, q=0.2)
    print("S=100, K=100, t=0, T=0.5, sigma=0.2, r=0.01, q=0.5 => Call [{}], Put [{}]".format(call_option, put_option))
