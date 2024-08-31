from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = Counter(s)
        t1 = Counter(t)

        for key in s1:
            if key not in t1:
                return False
            if s1[key] > t1[key]:
                return False
        
        return True