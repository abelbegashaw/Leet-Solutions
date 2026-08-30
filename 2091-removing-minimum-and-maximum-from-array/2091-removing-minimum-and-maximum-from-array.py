class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        max_index = nums.index(max(nums)) # 1
        min_index = nums.index(min(nums)) # 5
        

        return min (
            max(min_index, max_index) + 1,
            len(nums) - min(min_index, max_index),
            min_index + 1 + len(nums) - max_index,
            max_index + 1 + len(nums) - min_index,
        )
        """
        2, 10, 7, 5, 4, 1, 8, 6
           |            |
           2            3
        
        locate the numbers first and last occurrence. Will the following four options 
        delete the max and min elements consistently ...
        
        left, left => max_index
        left, right => left_dist + right_dist
        right, left => right_dist + left_dist
        right, right => min_index

        """