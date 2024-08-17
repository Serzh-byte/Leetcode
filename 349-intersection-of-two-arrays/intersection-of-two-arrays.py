class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        if len(nums1) > len(nums2):
            difference = len(nums1)-len(nums2)
            for i in range(difference):
                nums2.append('a')
            
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    ans.append(nums1[i])
        elif len(nums1) < len(nums2):
            difference = len(nums2)-len(nums1)
            for i in range(difference):
                nums1.append('a')
            
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    ans.append(nums1[i])
        else:
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    ans.append(nums1[i])
        ans = set(ans)
        return list(ans)

        