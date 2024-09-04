class Solution(object):
    def minimumOperations(self, nums):
        dct = {}
        for i in nums:
            if i not in dct and i != 0:
                dct[i] = 1
            elif i in dct and i != 0:
                dct[i] += 1
        return len(dct)