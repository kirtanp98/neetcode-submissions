class Node:
    def __init__(self, key= -1, value=-1, next =None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [Node() for _ in range(1000)]

    def hash(self, key) -> int:
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        current = self.map[self.hash(key)]

        while current.next:
            if current.next.key == key:
                current.next.value = value
                return;
            current = current.next
        current.next = Node(key, value, None)


    def get(self, key: int) -> int:
        current = self.map[self.hash(key)].next

        if not current:
            return -1

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        current = self.map[self.hash(key)]

        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next
        print("removing")

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)