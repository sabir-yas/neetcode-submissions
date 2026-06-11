class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        # Why: store both key and value so when we evict a node
        # we know which key to remove from the hashmap.

        self.prev = self.next = None
        # Why: doubly linked list nodes need pointers in both directions
        # so we can remove a node in O(1).


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        # Why: maximum number of items allowed before eviction.

        self.cache = {}
        # Why: hashmap gives O(1) access from key -> node.

        self.left, self.right = Node(0, 0), Node(0, 0)
        # Why: dummy boundary nodes make insertion/removal easier.
        # No special cases for empty list or first/last node.

        self.left.next, self.right.prev = self.right, self.left
        # Why: initially the list is empty:
        # LEFT <-> RIGHT


    def remove(self, node):
        prev, nxt = node.prev, node.next
        # Why: grab the node's neighbors before disconnecting it.

        prev.next = nxt
        # Why: make the previous node skip over 'node'.

        nxt.prev = prev
        # Why: make the next node skip back over 'node'.
        #
        # Before:
        # A <-> node <-> C
        #
        # After:
        # A <-> C


    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        # Why: insert right before RIGHT.
        # This position represents "most recently used".

        prev.next = nxt.prev = node
        # Why: tell both neighboring nodes about the new node.
        #
        # B ----> node
        # RIGHT <---- node

        node.next, node.prev = nxt, prev
        # Why: tell the new node who its neighbors are.
        #
        # B <-> node <-> RIGHT


    def get(self, key: int) -> int:

        if key in self.cache:
            # Why: only return a value if the key exists.

            self.remove(self.cache[key])
            # Why: take the node out of its current position.

            self.insert(self.cache[key])
            # Why: move it to the MRU (most recently used) position.

            return self.cache[key].val
            # Why: return the stored value.

        return -1
        # Why: key doesn't exist.


    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])
            # Why: if key already exists,
            # remove old node before replacing it.

        self.cache[key] = Node(key, value)
        # Why: create/store a new node and let hashmap point to it.

        self.insert(self.cache[key])
        # Why: newly inserted items count as most recently used.

        if len(self.cache) > self.cap:
            # Why: cache exceeded capacity.

            lru = self.left.next
            # Why: first real node after LEFT is always
            # the least recently used item.

            self.remove(lru)
            # Why: remove LRU node from linked list.

            del self.cache[lru.key]
            # Why: remove corresponding hashmap entry too.