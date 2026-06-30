class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        window = dict()
        left = result = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            while len(window) == 3:
                result += len(s) - right
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
        return result
