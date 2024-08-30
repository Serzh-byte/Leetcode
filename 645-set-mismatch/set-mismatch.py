from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        ans = []

        for i in range(1, len(nums)+1):
            if frequency[i] > 1:
                ans.append(i)

        for i in range(1, len(nums)+1):
            if i not in frequency:
                ans.append(i)
        

        return ans