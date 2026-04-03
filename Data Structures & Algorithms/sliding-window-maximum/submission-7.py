from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        q = deque()
        for i in range(k):
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
        p = k
        res = [q[0]]
        for p in range(k, len(nums)):
            if q[0] == nums[p - k]:
                q.popleft()
            while q and q[-1] < nums[p]:
                q.pop()
            q.append(nums[p])
            res.append(q[0])
        return res