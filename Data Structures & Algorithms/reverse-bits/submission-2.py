class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for i in range(1, 33):
            tail_bit = n & 1
            out = out | (tail_bit << 32 - i)
            n = n >> 1
            print(f"*********{i}***********")
            print(f'n: {n:032b}')
            print(f'o: {out:032b}')
        return out

# pos = 32 - i