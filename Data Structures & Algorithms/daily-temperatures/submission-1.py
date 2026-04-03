class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0] * len(temperatures)
        for i, x in reversed(list(enumerate(temperatures))):
            while stack and x >= temperatures[stack[-1]]:
                stack.pop()
            out[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return out