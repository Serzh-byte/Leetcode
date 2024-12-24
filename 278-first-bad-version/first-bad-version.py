# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        s, e = 1, n

        while s <= e:
            m = s + (e-s)//2
            if not isBadVersion(m):
                s = m + 1
            else:
                e = m - 1
        return s