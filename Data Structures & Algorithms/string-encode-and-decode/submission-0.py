class Solution:

    def encode(self, strs: List[str]) -> str:
        lambda_char = "\u03BB"
        encoded = ''
        for i in strs:
            encoded += i + lambda_char
        return encoded


    def decode(self, s: str) -> List[str]:
        lambda_char = "\u03BB"
        decoded = []
        buffer = ''
        for i in s:
            if i != lambda_char:
                buffer += str(i)
            else:
                decoded.append(buffer)
                buffer = ''
        return decoded
            



