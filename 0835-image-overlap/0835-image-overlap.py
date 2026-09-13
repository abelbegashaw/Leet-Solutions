class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        n = len(img1)
        field = [[0 for _ in range(3*n - 2)] for _ in range(3*n - 2)]
        for i in range(n):
            for j in range(n):
                field[i + n - 1][j + n - 1] = img1[i][j]
        
        result = 0
        for i in range(2*n - 1):
            for j in range(2*n - 1):
                overlap = 0
                for r in range(n):
                    for c in range(n):
                        
                        if field[i + r][j + c] == img2[r][c] == 1:
                            overlap += 1
                result = max(overlap, result)
        return result