class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def backtrack(curr, options):
            if not options:
                result.append(curr.copy())
                return

            for i in range(len(options)):
                curr.append(options[i])
                options.pop(i)
                backtrack(curr, options)
                options.insert(i, curr.pop())
        
        backtrack([], nums)
        return result