class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        longest = 0
        store = set()  

        for r in range(n):
            while s[r] in store:
                store.remove(s[l])
                l += 1
            w = (r-l) + 1
            longest = max(longest, w) 
            store.add(s[r])

        return longest     