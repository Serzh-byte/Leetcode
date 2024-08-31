class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        common_elements = set(nums[0])
        
        for subarray in nums[1:]:
            common_elements &= set(subarray)

        result = sorted(common_elements)
        
        return result
