/**
 * @param {number} n
 * @return {number}
 */
var countCommas = function(n) {
    let result = 0;
    let curr = 1000;
    while(curr <= n) {
        result += n - curr + 1
        curr *= 1000
    }
    return result;
};