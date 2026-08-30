class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        max_index = nums.index(max(nums))
        min_index = nums.index(min(nums))

        if max_index < min_index:
            max_index, min_index = min_index, max_index
        

        return min (
            max(min_index, max_index) + 1,
            len(nums) - min(min_index, max_index),
            min_index + 1 + len(nums) - max_index,
        )