class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        a = len(s)
        b = len(t)
        score = 0

        while i < a and j < b:
            if s[i] == t[j]:
                i += 1
                j += 1
                score += 1
            else:
                j += 1

        if score < a:
            return False
        elif score == a:
            return True
        
