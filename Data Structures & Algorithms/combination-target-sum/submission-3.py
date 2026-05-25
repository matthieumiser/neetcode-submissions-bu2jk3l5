class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index, s, path):
            if s == target:
                result.append(path[:])
                return
            elif index == len(nums) or s > target:
                return

            path.append(nums[index])
            backtrack(index, s + nums[index], path)

            path.pop()
            backtrack(index + 1, s, path)
        backtrack(0, 0, [])
        return result

                
