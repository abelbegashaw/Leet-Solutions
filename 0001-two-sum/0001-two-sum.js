/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let hashmap = {};
    for(let index = 0; index < nums.length; index++) {
        if (target - nums[index] in hashmap) {
            return [hashmap[target - nums[index]], index]
        } else {
            hashmap[nums[index]] = index;
        }
    }
};