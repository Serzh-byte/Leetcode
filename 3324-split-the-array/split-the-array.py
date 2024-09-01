from collections import Counter

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        freq = Counter(nums)

        for value in freq.values():
            if value > 2:
                return False
        
        return True