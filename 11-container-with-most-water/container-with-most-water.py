class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l, r = 0, n - 1
        mx = 0
        while l <= r:
            area = (r-l) * min(height[l], height[r])
            if area > mx:
                mx = area
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return mx

        