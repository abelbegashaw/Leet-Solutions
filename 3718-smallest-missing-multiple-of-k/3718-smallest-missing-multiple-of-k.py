class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        i = 0
        multiplier = 1
        while i < len(nums) and nums[i] <= multiplier * k:
            if multiplier * k == nums[i]:
                multiplier += 1
            i += 1
        return multiplier * k