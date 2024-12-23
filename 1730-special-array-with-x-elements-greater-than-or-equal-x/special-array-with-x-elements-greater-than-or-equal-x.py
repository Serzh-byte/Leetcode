class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)  # Sort in descending order
        for x in range(len(nums) + 1):  # Check all possible values of x
            count = sum(1 for num in nums if num >= x)
            if count == x:  # If x matches the count, return it
                return x
        return -1  # If no such x exists, return -1
