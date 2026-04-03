class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+', '-', '*', '/'}
        stack = []
        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                if i == '+':
                    stack.append(stack.pop() + stack.pop())
                elif i == '-':
                    stack.append((-1 * stack.pop()) + stack.pop())
                elif i == '*':
                    stack.append(stack.pop() * stack.pop())
                elif i == '/':
                    print(stack)
                    stack.append(int((1 / stack.pop()) * stack.pop()))
                    print(stack)
        return int(stack[-1])