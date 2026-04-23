class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bottom = 0
        top = len(nums) - 1
        curr = top // 2
        while nums[curr] != target and curr not in (top, bottom):
            print(bottom, curr, top)
            if nums[curr] > target:
                top = curr
                curr = ((top - bottom) // 2) + bottom
            elif nums[curr] < target:
                bottom = curr
                curr = ((top - bottom) // 2) + bottom
        if nums[curr] == target:
            return curr
        elif nums[top] == target:
            return top
        elif nums[bottom] == target:
            return bottom
        return -1