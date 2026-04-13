from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.keyvalue = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyvalue[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        t = self.keyvalue[key].get(timestamp)
        res = ""

        if t:
            return t
        else:
            val = self.keyvalue[key]
            index = val.bisect_right(timestamp)

            if index > 0:
                print(index)
                closest_key = val.keys()[index - 1]
                return val[closest_key]
            return ""
        return t if t else ""
        
