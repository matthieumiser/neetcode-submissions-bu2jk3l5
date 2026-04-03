from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in hashmap.items():
            buckets[value].append(key)
        result = []
        for item in reversed(buckets):
            for i in item:
                if len(result) < k:
                    result.append(i)
        return result



        