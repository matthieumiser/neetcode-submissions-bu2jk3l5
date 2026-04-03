class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        rolling_char_count = [0] * 26
        first_char_count = [0] * 26
        for c in s1:
            first_char_count[ord(c) - ord('a')] += 1
        p1 = 0
        p2 = 0
        while p2 < len(s2):
            rolling_char_count[ord(s2[p2]) - ord('a')] += 1
            if p2 - p1 < len(s1) - 1:
                p2 += 1
            elif p2 - p1 == len(s1) - 1:
                if rolling_char_count == first_char_count:
                    return True
                rolling_char_count[ord(s2[p1]) - ord('a')] -= 1
                p1 += 1
                p2 += 1
        
        return False    


        