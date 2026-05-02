
class TimeMap:
    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].add_val(value, timestamp) 
        else:
            self.hashmap[key] = self.Item(value, timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        return self.hashmap[key].get_val(timestamp)

    class Item:
        def __init__(self, val, ts):
            self.ts_hash = {ts: val}
            self.ts_arr = [ts]

        def add_val(self, val, ts):
            self.ts_hash[ts] = val
            self.ts_arr.append(ts)

        def get_val(self, ts):
            if ts in self.ts_hash:
                return self.ts_hash[ts]
            elif self.ts_arr[0] > ts:
                return ""
            l, h = 0, len(self.ts_arr) - 1
            i = 0
            while l < h:
                m = (l + h) // 2
                if m + 1 < len(self.ts_arr) and self.ts_arr[m] <= ts and self.ts_arr[m + 1] > ts:
                    return self.ts_hash[self.ts_arr[m]]
                if self.ts_arr[m] < ts:
                    l = m + 1
                else:
                    h = m - 1
                i += 1 
            return self.ts_hash[self.ts_arr[l]]
                
        
