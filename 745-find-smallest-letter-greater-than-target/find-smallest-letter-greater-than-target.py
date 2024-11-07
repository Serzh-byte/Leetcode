class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            mid_v = letters[mid]

            if mid_v <= target:
                start = mid + 1
            else:
                end = mid - 1

        return letters[start % len(letters)]
