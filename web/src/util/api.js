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
export function europeanOption(optionType, S, K, T, sigma, r, q) {
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
