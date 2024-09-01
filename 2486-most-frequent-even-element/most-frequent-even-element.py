class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_counts = {num: nums.count(num) for num in nums if num % 2 == 0}
        
        if even_counts:
            max_value = max(even_counts.values())
            most_frequent_evens = [key for key, value in even_counts.items() if value == max_value]
            return min(most_frequent_evens)
        else:
            return -1