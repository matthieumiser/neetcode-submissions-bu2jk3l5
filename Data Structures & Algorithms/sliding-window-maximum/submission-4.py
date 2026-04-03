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
        p = k - 1
        res = []
        while p < len(nums):
            while q and q[-1] < nums[p]:
                q.pop()
            q.append(nums[p])
            res.append(q[0])
            if q[0] == nums[p - (k - 1)]:
                q.popleft()
            p += 1
        return res