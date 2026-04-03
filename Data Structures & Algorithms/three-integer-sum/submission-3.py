class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()
        for i, x in enumerate(nums):
            p1 = i
            p2 = len(nums) - 1
            
            while p1 < p2:
                if i != p1 and i != p2:
                    if (nums[p1] + nums[p2]) * -1 < x:
                        p2 -= 1
                    elif (nums[p1] + nums[p2]) * -1 > x:
                        p1 += 1
                    else:
                        output.add(tuple([nums[i], nums[p1], nums[p2]]))
                        p1 += 1
                        p2 -= 1
                elif i == p1:
                    p1 += 1
                elif i == p2:
                    p2 -= 1
        return list(output)

        