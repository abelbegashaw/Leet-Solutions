class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        def product(num):
            result = 1
            while num:
                result *= num % 10
                num //= 10
            return result
        
        while product(n) % t:
            n += 1
        return n
