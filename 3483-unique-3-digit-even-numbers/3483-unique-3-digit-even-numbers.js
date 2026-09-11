/**
 * @param {number[]} digits
 * @return {number}
 */
var totalNumbers = function(digits) {
    
    let numbers = new Set();
    for(let i = 0; i < digits.length; i++) {
        for(let j = 0; j < digits.length; j++) {
            for(let k = 0; k < digits.length; k++) {
                if (i != k && j != k && i != j) {
                    let number = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if (number > 99 && number % 2 == 0) {
                        numbers.add(number);
                    }
                }
            }
        }
    }
    return numbers.size;
};