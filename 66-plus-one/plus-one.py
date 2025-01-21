class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(char) for char in digits]
        number = ''.join(digits)
        number = int(number)
        number += 1
        number = str(number)
        number = list(number)
        number = [int(char) for char in number]
        return number