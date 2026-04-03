class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append('#')
            encoded.append(s)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        count_buf = []
        decoded = []
        i = 0
        while i < len(s):
            count_buf.append(s[i])
            if s[i] == '#':
                count = int(''.join(count_buf[:-1]))
                i += 1
                decoded.append(s[i:i + count])
                i += count
                count_buf = []
                continue

            i += 1 
        return decoded

            



