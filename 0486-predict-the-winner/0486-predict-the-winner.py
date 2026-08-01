class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def backtrack(score, left, right, turn):
            if left > right:
                return score

            if turn == 0:
                return max(
                    backtrack(score + nums[left], left + 1, right, 1 - turn), 
                    backtrack(score + nums[right], left, right - 1, 1 - turn), 
                )
            else:
                return min(
                    backtrack(score - nums[left], left + 1, right, 1 - turn), 
                    backtrack(score - nums[right], left, right - 1, 1 - turn),   
                )

            
    
        return backtrack(0, 0, len(nums) - 1, 0) >= 0
