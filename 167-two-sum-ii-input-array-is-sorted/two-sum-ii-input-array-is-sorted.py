class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        l, r = 0, n-1
        ans = []
        while l <= r:
            check = 0
            check = numbers[l] + numbers[r]
            if check < target:
                l += 1
            elif check > target:
                r -=1
            else:
                ans.extend([l+1,r+1])
                return ans
        