class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Separate even and odd numbers into two lists and concatenate them
        return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 != 0]
