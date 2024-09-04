from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        freq = dict(sorted(freq.items(), key=lambda item: (item[1], -item[0])))
        ans = []
        for key in freq.keys():
            next_key = key + 1
            if next_key in freq and freq[key] == freq[next_key]: 
                ans.extend([min(key, next_key)] * freq[key])
            else:
                ans.extend([key] * freq[key])
        return ans