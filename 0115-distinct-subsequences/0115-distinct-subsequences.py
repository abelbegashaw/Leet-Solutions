class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        table = [[0 if j != len(t) else 1 for j in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    table[i][j] = table[i + 1][j + 1] + table[i + 1][j]
                else:
                    table[i][j] = table[i + 1][j]
        return table[0][0]