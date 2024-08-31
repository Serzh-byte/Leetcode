from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequency = Counter(arr)
        ans = []
        for value in frequency.values():
            if value in ans:
                return False
            ans.append(value)
        
        return True
