from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = Counter(stones)
        ans = 0
        for char in jewels:
            if char in freq.keys():
                ans += freq[char]
        
        return ans