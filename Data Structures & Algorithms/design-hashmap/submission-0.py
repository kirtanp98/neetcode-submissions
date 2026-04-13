class MyHashMap:

    def __init__(self):
        self.array = []

    def put(self, key: int, value: int) -> None:
        keyArray = [k for k, _ in self.array]
        if key not in keyArray:
            print("adding", key, value)
            self.array.append((key, value))
            print("array", self.array)
        else:
            i = keyArray.index(key)
            self.array[i] = (key, value)


    def get(self, key: int) -> int:
        for k,v in self.array:
            if key == k:
                print("getting", key, v)
                return v
        print("no hit", key, -1)
        return -1

    def remove(self, key: int) -> None:
        remove = -1
        print("removing", key)
        for i, tup in enumerate(self.array):
            if tup[0] == key:
                remove = i
                break
        if remove > -1:
            self.array.pop(remove)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)