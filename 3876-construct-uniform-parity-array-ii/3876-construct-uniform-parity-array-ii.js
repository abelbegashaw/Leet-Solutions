/**
 * @param {number[]} nums1
 * @return {boolean}
 */
var uniformArray = function(nums1) {

    let minEven = Infinity
    let minOdd = Infinity
    
    nums1.forEach((num) => num%2 == 0 ? minEven = Math.min(minEven, num) : minOdd = Math.min(minOdd, num))

    /*
    1, 3, 4

    lets change to the polarity of the smallest number
    because if we are trying to change to the other polarity
    of the smallest number we will not be getting a value > 0

    lets say the smallest number polarity is even, can we change the smallest odd number to even? This is false we can't

    lets say the smallest number polarity is odd, can we change the smallest even number to odd?

    */

    return minOdd < minEven || minEven == Infinity || minOdd == Infinity
};