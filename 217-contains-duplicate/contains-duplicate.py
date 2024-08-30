from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        frequency = Counter(nums)
        for key in frequency:
            if frequency[key] >= 2:
                return True
        
        return False