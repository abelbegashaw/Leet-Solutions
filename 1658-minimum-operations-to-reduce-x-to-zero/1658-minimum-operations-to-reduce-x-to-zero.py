class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        
        target = sum(nums) - x
        if target < 0:
            return -1
        total = 0
        left = 0
        result = -1
        for right in range(len(nums)):
            total += nums[right]
            while total > target:
                total -= nums[left]
                left += 1
            if total == target:
                result = max(result, right - left + 1)
        return result if result == -1 else len(nums) - result