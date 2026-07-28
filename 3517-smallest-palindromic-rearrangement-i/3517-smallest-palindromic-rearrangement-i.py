class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        letters = [0 for _ in range(26)]
        for char in s:
            letters[ord(char) - ord('a')] += 1
        
        result = ['' for _ in range(len(s))]
        curr = 0
        for i in range(len(letters)):
            while letters[i] > 1:
                result[curr] = result[len(s) - curr - 1] = chr(i + 97)
                curr += 1
                letters[i] -= 2
        
        if len(s) % 2:
            result[len(s) // 2] = s[len(s) // 2]
        
        return ''.join(result)

