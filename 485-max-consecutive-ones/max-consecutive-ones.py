class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        max_l = 0
        while l <= r and r < len(nums):
            if nums[l] == 1 and nums[r] == 1:
                r += 1
                max_l = max(max_l,(r-l))
            elif nums[r] == 0:
                r += 1
                l = r

        return max_l
