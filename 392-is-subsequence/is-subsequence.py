class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a, b = 0, 0
        A, B = len(s), len(t)
        
        while a < A and b < B:
            if s[a] == t[b]:
                a += 1 
            b += 1  
        
        return a == A  
