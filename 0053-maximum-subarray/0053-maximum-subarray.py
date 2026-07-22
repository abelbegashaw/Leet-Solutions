class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        result = float("-inf")
        sum = 0
        for num in nums:
            sum = max(sum + num, num)
            result = max(result, sum)
        return result