class Solution:
    def hammingWeight(self, n: int) -> int:
        return (n ^ 0).bit_count()