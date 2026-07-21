class ListNode:
    def __init__(self, val=0, key=None, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        self._swap_to_end(self.hashmap[key])
        return self.hashmap[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].val = value
            self._swap_to_end(self.hashmap[key])
        else:
            self.hashmap[key] = ListNode(val=value, key=key)
            self._append_tail(self.hashmap[key])
        if len(self.hashmap) > self.capacity:
            self._evict()
    
    def _swap_to_end(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        self._append_tail(node)

    def _evict(self):
        node = self.head.next
        del self.hashmap[node.key]
        self.head.next = node.next
        node.next.prev = self.head

    def _append_tail(self, node):
        node.next, node.prev = self.tail, self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node