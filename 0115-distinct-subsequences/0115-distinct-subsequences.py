class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        memo = [[-1 for _ in range(len(t))] for _ in range(len(s))]
        def dp(i, j):
            if j == len(t):
                return 1

            if i == len(s):
                return 0

            if memo[i][j] == -1:

                if s[i] == t[j]:
                    memo[i][j] = dp(i + 1, j + 1) + dp(i + 1, j)
                
                else:
                    memo[i][j] = dp(i + 1, j)
            return memo[i][j]

        dp(0, 0)
        return memo[0][0]