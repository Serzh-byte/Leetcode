class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)

        intersect1 = set1 & set2
        intersect2 = set2 & set3
        intersect3 = set1 & set3
    
        result = intersect1 | intersect2 | intersect3
        
        return list(result)