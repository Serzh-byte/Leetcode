from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        seen = set()
        for key in freq.keys():
            if freq[key] == key:
                seen.add(key)
        
        return max(seen) if seen else -1
