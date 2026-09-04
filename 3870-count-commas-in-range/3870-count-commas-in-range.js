/**
 * @param {number} n
 * @return {number}
 */
var countCommas = function(n) {
    // works only up to 999,999
    return Math.max(0, n - 999)
};