/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumDeletions = function(nums) {
    let max_index = nums.indexOf(Math.max(... nums));
    let min_index = nums.indexOf(Math.min(... nums));

    if (min_index > max_index) {
        let total = min_index + max_index;
        min_index = total - min_index;
        max_index = total - max_index;
    }

    return Math.min(
        max_index + 1,
        nums.length - min_index,
        min_index + 1 + nums.length - max_index
    );
};