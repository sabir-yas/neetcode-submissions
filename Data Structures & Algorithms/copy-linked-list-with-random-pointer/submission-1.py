"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        #phase 1- just copying over the nodes
        oldToCopy= {None:None}
        
        curr = head
        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr= curr.next

        #phase 2- linking the nodes
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr =curr.next
        
        return oldToCopy[head]
        
