from collections import defaultdict
from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count_map = defaultdict(int)

        for num in nums:
            if num % 2 == 0:
                count_map[num] += 1
        
        if not count_map:
            return -1

        most_frequent = -1
        max_count = 0
        
        for num, count in count_map.items():
            if count > max_count or (count == max_count and num < most_frequent):
                max_count = count
                most_frequent = num
        
        return most_frequent
