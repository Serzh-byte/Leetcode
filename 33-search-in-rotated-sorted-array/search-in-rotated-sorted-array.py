class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            # Check if mid is the target
            if nums[mid] == target:
                return mid

            # Check if left side is sorted
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1  # target is in the left half
                else:
                    start = mid + 1  # target is in the right half
            # Otherwise, the right side is sorted
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1  # target is in the right half
                else:
                    end = mid - 1  # target is in the left half

        return -1  # target not found
