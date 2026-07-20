class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = 0
        y = 0
        for i in range(len(nums) + 1):
            print(i)
            if i < len(nums): x ^= nums[i]
            y ^= i
        return x ^ y
     