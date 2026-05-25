class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        result_set = set()

        def backtrack(index, s, path):
            if s == target:
                if tuple(path[:]) not in result_set:
                    result.append(path[:])
                    result_set.add(tuple(path[:]))
                return
            elif index == len(nums) or s > target:
                return

            path.append(nums[index])
            backtrack(index + 1, s + nums[index], path)
            backtrack(index, s + nums[index], path)

            path.pop()
            backtrack(index + 1, s, path)
        backtrack(0, 0, [])
        return result

                
