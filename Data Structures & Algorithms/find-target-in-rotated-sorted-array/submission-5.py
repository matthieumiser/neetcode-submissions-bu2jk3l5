class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        start = hi
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_idx = self.transform(nums, start, mid)
            if nums[mid_idx] == target:
                return mid_idx
            elif nums[mid_idx] < target:
                lo = mid + 1
            elif nums[mid_idx] > target:
                hi = mid - 1
                
        return -1
    def transform(self, nums, start, idx):
        l = len(nums) - 1
        if idx + start <= l:
            return idx + start
        else:
            return idx + start - len(nums)
        