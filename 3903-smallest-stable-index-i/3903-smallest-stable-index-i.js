/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var firstStableIndex = function(nums, k) {
    
    for(var i = 0; i < nums.length; i++) {
        var maxLeft = -Infinity, minRight = Infinity
        for(let j = 0; j <= i; j++) {
            maxLeft = Math.max(maxLeft, nums[j])
        }
        for(let k = i; k < nums.length; k++) {
            minRight = Math.min(minRight, nums[k])
        }
        if (maxLeft - minRight <= k) {
            return i
        }
    }
    return -1
};