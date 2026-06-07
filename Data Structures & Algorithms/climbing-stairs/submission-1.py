class Solution:
    def climbStairs(self, n: int) -> int:
        last_2 = deque([1, 2])
        if n <= 3:
            return n
        for i in range(n-2):
            print(last_2)
            last_2.append(sum(last_2))
            last_2.popleft()
        return last_2.pop()


            