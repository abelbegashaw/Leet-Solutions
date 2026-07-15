class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        num_1 = (2 + (n - 1) * 2) * n // 2
        num_2 = (4 + (n - 1) * 2) * n // 2
        
        return gcd(num_1, num_2)