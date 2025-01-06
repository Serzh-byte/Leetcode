class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        for char in operations:
            if char == 'C' and len(score) != 0:
                score.pop()
            elif char == 'D':
                score.append(int(score[-1]) * 2)
            elif char == '+':
                score.append(score[-1] + score[-2])
            else:
                score.append(int(char))
        
        return sum(score)