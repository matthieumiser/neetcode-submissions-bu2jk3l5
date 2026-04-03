class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        char_counts = [0] * 26
        p1 = 0
        p2 = 0
        replacements = 0
        while p2 < len(s):
            max_len = max(max_len, max(char_counts) + replacements) if replacements <= k else max_len
            if replacements <= k:
                char_counts[ord(s[p2]) - ord('A')] += 1
                p2 += 1
            else:
                char_counts[ord(s[p1]) - ord('A')] -= 1
                p1 += 1
            replacements = p2 - p1 - max(char_counts)
        max_len = max(max_len, max(char_counts) + replacements) if replacements <= k else max_len
            
        return max_len

            

            