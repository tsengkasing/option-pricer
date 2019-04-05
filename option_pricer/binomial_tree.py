# Implement the Binomial Tree method for American call/put options

import numpy as np

def american_call_binomial_tree(s_0, sigma, r, T, K, N):
    """Calculate the value of American call option by the method of
    Binomial Tree.

    Args:
        s_0: The value of asset S at time 0
        sigma: The volatility
        r: The risk-free rate
        T: The time to maturity(in years)
        K: Strike
        N: The number of steps in Binomial Tree

    Returns:
        The American call option value
    """
    def _calculate_node_value(v_0, remain_layer):
        """Calculate the option value at this node

        Args:
            v_0: The stock price at this node
            remain_layer: The remaining layer number from leaf node

        Returns:
            The call option value at this node
        """
        if remain_layer <= 0:
            return max(v_0-K, 0)
        else:
            return max(v_0-K, _DF*(_p*_calculate_node_value(v_0*_u, remain_layer-1)
                              + (1-_p)*_calculate_node_value(v_0*_d, remain_layer-1)))

    _delta_T = T/N
    _u = np.exp(sigma*np.sqrt(_delta_T))
    _d = 1/_u
    _p = (np.exp(r*_delta_T)-_d)/(_u-_d)
    _DF = np.exp(-r*_delta_T) # discount factor DF = e^(-r*deltaT)

    return _calculate_node_value(s_0, N)

def american_put_binomial_tree(s_0, sigma, r, T, K, N):
    """Calculate the value of American put option by the method of
    Binomial Tree.

    Args:
        s_0: The value of asset S at time 0
        sigma: The volatility
        r: The risk-free rate
        T: The time to maturity(in years)
        K: Strike
        N: The number of steps in Binomial Tree

    Returns:
        The American put option value
    """
    def _calculate_node_value(v_0, remain_layer):
        """Calculate the option value at this node

        Args:
            v_0: The stock price at this node
            remain_layer: The remaining layer number from leaf node

        Returns:
            The put option value at this node
        """
        if remain_layer <= 0:
            return max(K-v_0, 0)
        else:
            return max(K-v_0, _DF*(_p*_calculate_node_value(v_0*_u, remain_layer-1)
                              + (1-_p)*_calculate_node_value(v_0*_d, remain_layer-1)))

    _delta_T = T/N
    _u = np.exp(sigma*np.sqrt(_delta_T))
    _d = 1/_u
    _p = (np.exp(r*_delta_T)-_d)/(_u-_d)
    _DF = np.exp(-r*_delta_T) # discount factor DF = e^(-r*deltaT)

    return _calculate_node_value(s_0, N)

def main():
    K = 52
    T = 2
    r = 0.05
    sigma = 0.223144
    s_0 = 50
    N = 2
    print("American put value: " + str(american_put_binomial_tree(s_0, sigma, r, T, K, N)))

    K = 50
    T = 0.25
    r = 0.05
    sigma = 0.3
    s_0 = 50
    N = 1
    print("American call value: " + str(american_call_binomial_tree(s_0, sigma, r, T, K, N)))

    N = 2
    print("American call value: " + str(american_call_binomial_tree(s_0, sigma, r, T, K, N)))
    
    N = 3
    print("American call value: " + str(american_call_binomial_tree(s_0, sigma, r, T, K, N)))


if __name__ == '__main__':
    main()