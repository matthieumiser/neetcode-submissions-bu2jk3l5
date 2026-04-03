class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        longest = 0
        hashset = set()
        while end < len(s):
            if s[end] not in hashset:
                hashset.add(s[end])
                longest = max(len(hashset), longest)
                end += 1
            else:
                hashset.discard(s[start])
                start += 1

        return longest