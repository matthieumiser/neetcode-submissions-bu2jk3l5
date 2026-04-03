class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        p1 = 0
        p2 = 0
        t_map = defaultdict(int)
        for c in t:
            t_map[c] += 1
        s_map = defaultdict(int)
        window_ptrs = [p1, p2]
        smallest_window = float('inf')
        is_found = False
        while p2 < len(s):
            if s[p2] in t_map:
                s_map[s[p2]] += 1

            while self.valsGt(s_map, t_map):
                is_found = True
                if p2 - p1 < smallest_window:
                    window_ptrs = [p1, p2]
                    smallest_window = p2 - p1
                if s_map[s[p1]] > 0:
                    s_map[s[p1]] -= 1
                else:
                    del s_map[s[p1]]
                p1 += 1
            p2 += 1
        if is_found: return s[window_ptrs[0]:window_ptrs[1]+1]
        else: return ''
    def valsGt(self, s, t):
        if len(s) != len(t):
            return False
        for key, val in s.items():
            if val < t[key]:
                return False
        return True