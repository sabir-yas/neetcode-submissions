class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache ={} #self.cache
        
        #left=LRU, right=most recent
        self.left, self.right= Node(0,0), Node(0,0) #dummy nodes
        self.left.next = self.right # initially need to be connected to insert into
        self.right.prev = self.left

    #remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    #insert node at right
    def insert(self,node):
        prev, nxt= self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache: # remember need to update to most recent if get
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val #tells us the node, need to get val,
        return -1    

    def put(self, key: int, value: int) -> None:
        if key in self.cache: # a node already exists with the same key value
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            #remove and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]