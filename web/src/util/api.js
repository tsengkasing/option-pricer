/**
 * @fileoverview
 * API list
 */

/**
 * European Option
 * @param {string} optionType 'call' | 'put'
 * @param {number} S
 * @param {number} K
 * @param {number} T
 * @param {number} sigma
 * @param {number} r
 * @param {number} q
 */
export function calcEuropeanOption(optionType, S, K, T, sigma, r, q) {
    return new Promise((resolve, reject) => {
        fetch(`/api/european_option/${optionType}?S=${S}&K=${K}&T=${T}&sigma=${sigma}&r=${r}&q=${q}`, {
            method: 'GET',
        }).then(
            response => response.json()
        ).then(({status, msg, data}) => {
            if (status === 0) {
                resolve(data);
            } else {
                reject(msg);
            }
        }).catch(err => reject(err));
    });
}

/**
 * Implied Volatility
 * @param {string} optionType 'call' | 'put'
 * @param {number} S
 * @param {number} K
 * @param {number} T
 * @param {number} r
 * @param {number} q
 * @param {number} optionPremium
 */
export function calcImpliedVolatility(optionType, S, K, T, r, q, optionPremium) {
    return new Promise((resolve, reject) => {
        fetch(`/api/implied_volatility/${optionType}?S=${S}&K=${K}&T=${T}&optionPremium=${optionPremium}&r=${r}&q=${q}`, {
            method: 'GET',
        }).then(
            response => response.json()
        ).then(({status, msg, data}) => {
            if (status === 0) {
                resolve(data);
            } else {
                reject(msg);
            }
        }).catch(err => reject(err));
    });
}

/**
 * American Option
 * @param {string} optionType 'call' | 'put'
 * @param {number} S
 * @param {number} sigma
 * @param {number} r
 * @param {number} T
 * @param {number} K
 * @param {number} N
 */
export function calcAmericanOption(optionType, S, sigma, r, T, K, N) {
    return new Promise((resolve, reject) => {
        fetch(`/api/american_option/${optionType}?S=${S}&K=${K}&T=${T}&sigma=${sigma}&r=${r}&N=${N}`, {
            method: 'GET',
        }).then(
            response => response.json()
        ).then(({status, msg, data}) => {
            if (status === 0) {
                resolve(data);
            } else {
                reject(msg);
            }
        }).catch(err => reject(err));
    });
}

/**
 * Geometric Asian option
 * @param {string} optionType 'call' | 'put'
 * @param {number} S
 * @param {number} sigma
 * @param {number} r
 * @param {number} T
 * @param {number} K
 * @param {number} n
 */
export function calcGeometricAsianOption(optionType, S, sigma, r, T, K, n) {
    return new Promise((resolve, reject) => {
        fetch(`/api/geometric_asian_option/${optionType}?S=${S}&K=${K}&T=${T}&sigma=${sigma}&r=${r}&n=${n}`, {
            method: 'GET',
        }).then(
            response => response.json()
        ).then(({status, msg, data}) => {
            if (status === 0) {
                resolve(data);
            } else {
                reject(msg);
            }
        }).catch(err => reject(err));
    });
}

/**
 * Arithmetic Asian option
 * @param {string} optionType 'call' | 'put'
 * @param {number} S
 * @param {number} sigma
 * @param {number} r
 * @param {number} T
 * @param {number} K
 * @param {number} n
 * @param {number} m
 * @param {number} control 0 | 1
 * @param {number} seed
 */
export function calcArithmeticAsianOption(optionType, S, sigma, r, T, K, n, m, control, seed) {
    return new Promise((resolve, reject) => {
        fetch(`/api/arithmetic_asian_option/${optionType}?S=${S}&K=${K}&T=${T}&sigma=${sigma}&r=${r}&n=${n}&m=${m}&control=${control}&seed=${seed}`, {
            method: 'GET',
        }).then(
            response => response.json()
        ).then(({status, msg, data}) => {
            if (status === 0) {
                resolve(data);
            } else {
                reject(msg);
            }
        }).catch(err => reject(err));
    });
}

/**
 * Geometric basket option
 * @param {string} optionType 'call' | 'put'
 * @param {number} S1
 * @param {number} S2
 * @param {number} sigma1
 * @param {number} sigma2
 * @param {number} r
 * @param {number} T
 * @param {number} K
 * @param {number} correlation
 */
export function calcGeometricBasketOption(optionType, S1, S2, sigma1, sigma2, r, T, K, correlation) {
    return new Promise((resolve, reject) => {
        fetch(`/api/geometric_basket_option/${optionType}?S1=${S1}&S2=${S2}&sigma1=${sigma1}&sigma2=${sigma2}&K=${K}&T=${T}&r=${r}&rho=${correlation}`, {
            method: 'GET',
        }).then(
            response => response.json()
        ).then(({status, msg, data}) => {
            if (status === 0) {
                resolve(data);
            } else {
                reject(msg);
            }
        }).catch(err => reject(err));
    });
}

/**
 * Arithmetic Basket Option
 * @param {string} optionType 'call' | 'put'
 * @param {number} S1
 * @param {number} S2
 * @param {number} sigma1
 * @param {number} sigma2
 * @param {number} r
 * @param {number} T
 * @param {number} K
 * @param {number} correlation
 * @param {number} m
 * @param {number} control 0 | 1
 * @param {number} seed
 */
export function calcArithmeticBasketOption(optionType, S1, S2, sigma1, sigma2, r, T, K, correlation, m, control, seed) {
    return new Promise((resolve, reject) => {
        fetch(`/api/arithmetic_basket_option/${optionType}?S1=${S1}&S2=${S2}&sigma1=${sigma1}&sigma2=${sigma2}&K=${K}&T=${T}&r=${r}&rho=${correlation}&m=${m}&control=${control}&seed=${seed}`, {
            method: 'GET',
        }).then(
            response => response.json()
        ).then(({status, msg, data}) => {
            if (status === 0) {
                resolve(data);
            } else {
                reject(msg);
            }
        }).catch(err => reject(err));
    });
}
