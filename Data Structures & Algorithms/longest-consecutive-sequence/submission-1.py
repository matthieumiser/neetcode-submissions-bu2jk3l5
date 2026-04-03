class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        curr_len = 1
        max_len = 1
        in_seq = False
        if len(nums) == 0:
            return 0
        for i, x in enumerate(nums):
            ptr = x
            while ptr + 1 in hashset:
                ptr += 1
                curr_len += 1
            if curr_len > max_len:
                max_len = curr_len
            curr_len = 1
        return max_len

