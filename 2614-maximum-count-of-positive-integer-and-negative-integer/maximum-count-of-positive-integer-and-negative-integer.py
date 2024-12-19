from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Find the first positive number using binary search
        start, end = 0, n - 1
        first_positive = n  # Default to n if no positive number is found
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] > 0:
                first_positive = mid  # Update to current index
                end = mid - 1  # Search the left half
            else:
                start = mid + 1  # Search the right half

        # Find the last negative number using binary search
        start, end = 0, n - 1
        last_negative = -1  # Default to -1 if no negative number is found
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] < 0:
                last_negative = mid  # Update to current index
                start = mid + 1  # Search the right half
            else:
                end = mid - 1  # Search the left half

        # Calculate counts
        positive_count = n - first_positive
        negative_count = last_negative + 1

        # Return the maximum count
        return max(positive_count, negative_count)
