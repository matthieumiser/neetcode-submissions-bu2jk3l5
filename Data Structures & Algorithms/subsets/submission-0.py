class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(index, path):
            if index == len(nums):
                result.append(path[:])
                return

            # move forward
            path.append(nums[index])
            backtrack(index + 1, path)

            # move backward 
            path.pop()
            backtrack(index + 1, path)
        backtrack(0, [])
        return result
