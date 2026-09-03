class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        # 2 2 2
        # 0 0 2
        # 2 2 0
        maximum, minimum = nums[:], nums[:]
        for i in range(1, len(nums)):
            maximum[i] = max(maximum[i - 1], maximum[i])
        for i in range(len(nums) - 2, -1, -1):
            minimum[i] = min(minimum[i], minimum[i + 1])
        index = float("inf")
        for i in range(len(nums)):
            if maximum[i] - minimum[i] <= k:
                index = min(index, i)
        return index if index != float("inf") else -1
