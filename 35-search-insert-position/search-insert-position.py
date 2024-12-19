class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            mid_value = nums[mid]

            if mid_value == target:
                return mid
            elif target < mid_value:
                end = mid - 1
            else:
                start = mid + 1

        return start
