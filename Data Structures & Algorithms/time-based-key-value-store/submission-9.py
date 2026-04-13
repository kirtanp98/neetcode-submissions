from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.keyvalue = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.keyvalue[key]:
            self.keyvalue[key][timestamp] = value
        else:
            self.keyvalue[key] = {timestamp:value}
        

    def get(self, key: str, timestamp: int) -> str:
        t = self.keyvalue[key].get(timestamp)
        res = ""

        if t:
            return t
        else:
            val = list(self.keyvalue[key].keys())
            l,r = 0, len(val) -1
            while l <= r:
                mid = (l +r) //2
                if val[mid] == timestamp:
                    return self.keyvalue[key][val[mid]]

                if val[mid] < timestamp:
                    res= self.keyvalue[key].get(val[mid])
                    l = mid + 1
                else:
                    r = mid -1
                        
            return res
        return t if t else ""
        
