class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        # link the doubly list
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        
        node = self.node_map[key]

        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            old_node = self.node_map[key]
            self.remove(old_node)
        node = ListNode(key, value)
        self.node_map[key] = node
        self.insert(node)

        if len(self.node_map) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.node_map[node_to_delete.key]
    
    def insert(self, node):
        prev_end = self.tail.prev
        prev_end.next = node

        node.prev = prev_end
        node.next = self.tail

        self.tail.prev = node
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev