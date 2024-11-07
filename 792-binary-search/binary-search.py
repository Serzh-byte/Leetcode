class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1

        while start <= end:
            midpoint = start +(end-start)//2
            midpoint_value = nums[midpoint]

            if midpoint_value == target:
                return midpoint
            
            elif target < midpoint_value:
                end = midpoint - 1
            else:
                start = midpoint + 1

        return -1
            
