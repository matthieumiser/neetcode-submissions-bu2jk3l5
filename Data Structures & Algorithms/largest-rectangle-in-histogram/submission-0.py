class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # left to right, monotonic stack records indices of the next greatest item to the left
        # right to left, monotonic stack records indices of the next greatest item to the right
        # go through the array again and use the two arrays created above to decide the largest rectangle

        stack = []
        next_greatest = [None] * len(heights)
        for i, x in enumerate(heights):
            while stack and heights[stack[-1]] > x:
                popped = stack.pop()
                next_greatest[popped] = i
            stack.append(i)
        
        stack = []
        prev_greatest = [None] * len(heights)
        for i, x in reversed(list(enumerate(heights))):
            while stack and heights[stack[-1]] > x:
                popped = stack.pop()
                prev_greatest[popped] = i
            stack.append(i)
        
        max_rec = 0
        print(next_greatest)
        print(prev_greatest)

        for i, x in enumerate(heights):
            nextus = next_greatest[i] if next_greatest[i] != None else len(heights)
            prevus = prev_greatest[i] if prev_greatest[i] != None else -1
            print(nextus, prevus,(nextus - prevus - 1))

            max_rec = max((nextus - prevus - 1) * x, max_rec)

        return max_rec