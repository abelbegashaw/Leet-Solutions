class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        for i in range(len(nums)):
            maxLeft, minRight = -float("inf"), float("inf")
            for j in range(i + 1):
                maxLeft = max(maxLeft, nums[j])
            for j in range(i, len(nums)):
                minRight = min(minRight, nums[j])
            if maxLeft - minRight <= k:
                return i
        return -1