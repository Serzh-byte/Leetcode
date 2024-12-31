class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]  # Start by assuming the first element is the closest.
        
        for num in nums:

            if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
                closest = num
        
        return closest
