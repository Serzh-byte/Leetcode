class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        lenres = 0

        def check(l, r):
            nonlocal result, lenres
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > lenres:
                    result = s[l:r+1]
                    lenres = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            # Check for odd-length palindromes
            check(i, i)
            # Check for even-length palindromes
            check(i, i + 1)
        
        return result
