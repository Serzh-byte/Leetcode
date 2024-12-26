class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums = sorted(nums)
        closest_sum = float('inf')  
        
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s

                if abs(target - s) < abs(target - closest_sum):
                    closest_sum = s
                
                if s < target:
                    l += 1
                else:
                    r -= 1
        
        return closest_sum  
