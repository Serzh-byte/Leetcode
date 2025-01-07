class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n
        for index, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_ind = stack.pop()
                ans[prev_ind] = index - prev_ind
            stack.append(index)

        return ans

                
