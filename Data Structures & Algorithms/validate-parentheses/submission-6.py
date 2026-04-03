class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        if len(s) % 2 > 0:
            return False
        opening = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in opening:
                stack.append(c)
            elif stack and c != opening[stack[-1]]:
                return False
            else:
                if not stack:
                    return False
                stack.pop()
        if not stack:
            return True 
        return False

