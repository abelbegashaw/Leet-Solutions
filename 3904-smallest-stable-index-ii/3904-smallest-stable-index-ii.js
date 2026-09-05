/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var firstStableIndex = function(nums, k) {
    var maxLeft = Array.from({length : nums.length}, (_, i) => nums[i])
    var minRight = Array.from({length : nums.length}, (_, i) => nums[i])
    for(let i = 1; i < maxLeft.length; i++) {
        maxLeft[i] = Math.max(maxLeft[i], maxLeft[i - 1])
    }
    for(let i = minRight.length - 2; i > -1; i--) {
        minRight[i] = Math.min(minRight[i], minRight[i + 1])
    }
    for(let i = 0; i < nums.length; i++) {
        if(maxLeft[i] - minRight[i] <= k) {
            return i
        }
    }
    return -1
};