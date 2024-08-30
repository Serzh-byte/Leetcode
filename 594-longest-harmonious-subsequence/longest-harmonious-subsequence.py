class Solution:
    def findLHS(self, nums: List[int]) -> int:
        frequency = {num: nums.count(num) for num in set(nums)}
        
        max_length = 0 
        for key in frequency:
            if key + 1 in frequency:
                length = frequency[key] + frequency[key + 1]
                max_length = max(max_length, length)
        
        return max_length