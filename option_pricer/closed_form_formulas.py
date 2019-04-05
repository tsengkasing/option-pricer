# -*- coding: utf-8 -*-

# Implemented:
# 1 closed-form formulas for geometric Asian call/put options
# 2 closed-from formulas for geometric basket call/put options

import numpy as np
from scipy.stats import norm

def geom_asian_call_option(s_t, sigma, r, T, K, n, t=0):
    """Calculate the value of geometric Asian call option. By default 
    calculate the value at time 0.

    Args:
        s_t: The value of asset S at time t
        sigma: The volatility
        r: The risk-free rate
        T: The time to maturity(in years)
        K: Strike
        n: The number of observation times for geometric average n
        t: Time t for option value, default 0

    Returns:
        The geometric Asian call option value at time t
    """
    _T = T-t

    _sigma_hat_sq_T = sigma*sigma*(n+1)*(2*n+1)/(6*n*n)*_T # (sigma^2)*T, convience for latter calculation
    _mu_hat_T = (r-0.5*sigma*sigma)*(n+1)/(2*n)*_T + 0.5*_sigma_hat_sq_T # mu*T, convience for latter calculation

    _d1 = (np.log(s_t/K) + _mu_hat_T + 0.5*_sigma_hat_sq_T) / (np.sqrt(_sigma_hat_sq_T))
    _d2 = _d1 - np.sqrt(_sigma_hat_sq_T)

    _N1 = norm.cdf(_d1)
    _N2 = norm.cdf(_d2)

    return np.exp(-r*_T)*(s_t*np.exp(_mu_hat_T)*_N1 - K*_N2)

def geom_asian_put_option(s_t, sigma, r, T, K, n, t=0):
    """Calculate the value of geometric Asian put option. By default 
    calculate the value at time 0.

    Args:
        s_t: The value of asset S at time t
        sigma: The volatility
        r: The risk-free rate
        T: The time to maturity(in years)
        K: Strike
        n: The number of observation times for geometric average n
        t: Time t for option value, default 0

    Returns:
        The geometric Asian put option value at time t
    """
    _T = T-t

    _sigma_hat_sq_T = sigma*sigma*(n+1)*(2*n+1)/(6*n*n)*_T # (sigma^2)*T, convience for latter calculation
    _mu_hat_T = (r-0.5*sigma*sigma)*(n+1)/(2*n)*_T + 0.5*_sigma_hat_sq_T # mu*T, convience for latter calculation

    _d1 = (np.log(s_t/K) + _mu_hat_T + 0.5*_sigma_hat_sq_T) / (np.sqrt(_sigma_hat_sq_T))
    _d2 = _d1 - np.sqrt(_sigma_hat_sq_T)

    _N1 = norm.cdf(-_d1)
    _N2 = norm.cdf(-_d2)

    return np.exp(-r*_T)*(K*_N2 - s_t*np.exp(_mu_hat_T)*_N1)

def geom_basket_call_option(s_t_1, s_t_2, sigma_1, sigma_2, r, T, K, rho, t=0):
    """Calculate the value of geometric basket call option. By default 
    calculate the value at time 0.

    Args:
        s_t_1: The value of asset S1 at time t
        s_t_2: The value of asset S2 at time t
        sigma_1: The volatility of S1
        sigma_2: The volatility of S2
        r: The risk-free rate
        T: The time to maturity(in years)
        K: Strike
        rho: The correlation rho
        t: Time t for option value, default 0

    Returns:
        The geometric basket call option value at time t
    """
    _T = T-t

    _sigma_sq_T = (2*sigma_1*sigma_2*rho + sigma_1*sigma_1 + \
        sigma_2*sigma_2) / (2*2) *_T # (sigma^2)*T, convience for latter calculation
    _mu_T = r*_T - 0.5*(sigma_1*sigma_1+sigma_2*sigma_2)/2*_T + 0.5*_sigma_sq_T

    _B_t = np.sqrt(s_t_1*s_t_2)

    _d1 = (np.log(_B_t/K) + _mu_T + 0.5*_sigma_sq_T) / (np.sqrt(_sigma_sq_T))
    _d2 = _d1 - np.sqrt(_sigma_sq_T)

    _N1 = norm.cdf(_d1)
    _N2 = norm.cdf(_d2)

    return np.exp(-r*_T)*(_B_t*np.exp(_mu_T)*_N1 - K*_N2)

def geom_basket_put_option(s_t_1, s_t_2, sigma_1, sigma_2, r, T, K, rho, t=0):
    """Calculate the value of geometric basket call option. By default 
    calculate the value at time 0.

    Args:
        s_t_1: The original value of asset S1
        s_t_2: The original value of asset S2
        sigma_1: The volatility of S1
        sigma_2: The volatility of S2
        r: The risk-free rate
        T: The time to maturity(in years)
        K: Strike
        rho: The correlation rho
        t: Time t for option value, default 0

    Returns:
        The geometric basket call option value at time t
    """
    _T = T-t

    _sigma_sq_T = (2*sigma_1*sigma_2*rho + sigma_1*sigma_1 + \
        sigma_2*sigma_2) / (2*2) *_T # (sigma^2)*T, convience for latter calculation
    _mu_T = r*_T - 0.5*(sigma_1*sigma_1+sigma_2*sigma_2)/2*_T + 0.5*_sigma_sq_T

    _B_t = np.sqrt(s_t_1*s_t_2)

    _d1 = (np.log(_B_t/K) + _mu_T + 0.5*_sigma_sq_T) / (np.sqrt(_sigma_sq_T))
    _d2 = _d1 - np.sqrt(_sigma_sq_T)

    _N1 = norm.cdf(-_d1)
    _N2 = norm.cdf(-_d2)

    return np.exp(-r*_T)*(K*_N2 - _B_t*np.exp(_mu_T)*_N1)

def main():
    s_t = 100
    sigma = 0.3
    r = 0.05
    T = 3
    K = 100
    n = 50

    print('Asian call: ' + str(geom_asian_call_option(s_t, sigma, r, T, K, n)))
    print('Asian put: ' + str(geom_asian_put_option(s_t, sigma, r, T, K, n)))

    s_t_1 = 100
    s_t_2 = 100
    sigma_1 = 0.3
    sigma_2 = 0.3
    K = 100
    rho = 0.5
    
    print('Basket call: ' + str(geom_basket_call_option(s_t_1, s_t_2, sigma_1, sigma_2, r, T, K, rho)))
    print('Basket put: ' + str(geom_basket_put_option(s_t_1, s_t_2, sigma_1, sigma_2, r, T, K, rho)))

if __name__ == '__main__':
    main()