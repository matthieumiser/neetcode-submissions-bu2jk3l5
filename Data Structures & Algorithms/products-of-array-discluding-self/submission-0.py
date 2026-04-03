class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [None] * len(nums)
        suffix = [None] * len(nums)

        for i, x in enumerate(nums):
            if i == 0:
                prefix[i] = 1
                continue
            elif i == 1:
                prefix[i] = nums[i-1]
            else:
                prefix[i] = nums[i-1] * prefix[i-1]

        for idx, x in enumerate(reversed(nums)):
            i = len(nums) - 1 - idx
            if idx == 0:
                suffix[i] = 1
                continue
            elif idx == 1:
                suffix[i] = nums[i+1]
            else:
                suffix[i] = nums[i+1] * suffix[i+1]
        
        result = []
        for i, x in enumerate(nums):
            result.append(prefix[i] * suffix[i])

        return result