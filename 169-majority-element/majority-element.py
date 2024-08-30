from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        compare = len(nums)/2
        for key in frequency:
            if frequency[key] > compare:
                return key
        

        