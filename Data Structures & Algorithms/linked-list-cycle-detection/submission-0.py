# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        '''
        hashset solution- O(n) time and O(n) memory(due to posibility of adding every element in list)
        hashSet = set()

        while head:
            if head.next in hashSet:
                return True
            hashSet.add(head.next)
            head = head.next
        
        return False
        '''
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

