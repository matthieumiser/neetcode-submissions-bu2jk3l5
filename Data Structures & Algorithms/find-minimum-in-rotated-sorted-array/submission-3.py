class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        while lo <= hi:
            mid = (hi + lo) // 2
            if nums[mid - 1] > nums[mid] < nums[mid + 1] if len(nums) - 1 > mid else float('inf'):
                return nums[mid]
            elif nums[mid] > nums [hi]:
                lo = mid + 1
            elif nums[mid] < nums[lo] or nums[lo] < nums[mid] < nums[hi]:
                hi = mid - 1
        return nums[mid]

