/**
 * @param {number} n
 * @return {number}
 */
var countCommas = function(n) {
    let result = 0;
    let curr = 999;
    let commas = 1;
    while (curr <= n) {
        let next = curr * 1000 + 999
        if (next <= n) {
            result += (next - curr) * commas
        } else {
            result += (n - curr) * commas
        }
        curr = next
        commas++;
    }
    return result;
};