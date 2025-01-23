from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        n = len(nums)

        for key in freq.keys():
            if freq[key] > n/2:
                return key