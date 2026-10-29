from dataclasses import dataclass

@dataclass
class DNode:
    key: int
    value: int
    prev: "DNode| None" = None
    next: "DNode| None" = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map: dict[int, DNode] = {}
        self.head = DNode(0,0)
        self.tail = DNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map[key]
        self.remove(node)
        self.add_to_back(node)
        return node.value

    def add_to_back(self, node: DNode) -> None:
        last = self.tail.prev
        node.prev = last
        node.next = self.tail
        last.next = node 
        self.tail.prev = node   

    def remove(self, node: DNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.remove(node)
            self.add_to_back(node)
            return
        else:
            new_node = DNode(key, value)
            self.add_to_back(new_node)
            self.map[key] = new_node
            if len(self.map) > self.capacity:
                lru = self.head.next
                self.remove(lru)
                del self.map[lru.key]
                
        
