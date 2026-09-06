class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        memo = {}
        def dp(i, j):
            if j == len(t):
                return 1

            if i == len(s):
                return 0
            
            state = (i, j)
            if state not in memo:

                if s[i] == t[j]:
                    memo[state] = dp(i + 1, j + 1) + dp(i + 1, j)
                
                else:
                    memo[state] = dp(i + 1, j)
            return memo[state]

        return dp(0, 0)