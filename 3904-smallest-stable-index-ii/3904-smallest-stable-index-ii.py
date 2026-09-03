class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        maximum, minimum = nums[:], nums[:]
        for i in range(1, len(nums)):
            maximum[i] = max(maximum[i - 1], maximum[i])
        for i in range(len(nums) - 2, -1, -1):
            minimum[i] = min(minimum[i], minimum[i + 1])
        
        for i in range(len(nums)):
            if maximum[i] - minimum[i] <= k:
                return i
        return -1
