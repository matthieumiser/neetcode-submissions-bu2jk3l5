class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        first = True
        while slow != fast or first:
            print(slow, fast)
            slow = nums[slow]
            fast = nums[nums[fast]]
            first = False
        slow = 0
        i = 0
        while slow != fast and i < 10000:
            slow = nums[slow]
            fast = nums[fast]
            i += 1
        return slow
