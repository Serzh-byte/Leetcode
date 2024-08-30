class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        number_map = {num: True for num in nums}
        
        n = len(nums)
        ans = []
        
        
        for i in range(1, n + 1):
            if i not in number_map:
                ans.append(i)
        
        return ans