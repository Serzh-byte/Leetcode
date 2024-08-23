class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()  
        left, right = 0, len(nums) - 1
        
        while left < right:
            if abs(nums[left]) < abs(nums[right]):
                right -= 1
            elif abs(nums[left]) > abs(nums[right]):
                left += 1
            else:
                if nums[right] > 0 and nums[left] < 0:  
                    return nums[right]
                left += 1
                right -= 1
        
        return -1  
