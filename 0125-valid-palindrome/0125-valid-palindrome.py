class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        chars = []
        for char in s:
            if char.isalnum():
                chars.append(char.lower())
        
        left, right = 0, len(chars) - 1
        while left <= right and chars[left] == chars[right]:
            left, right = left + 1, right - 1

        return left > right
