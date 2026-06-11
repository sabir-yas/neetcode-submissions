# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        '''
        looking at reversing entire list

        while r < len(nums):
        prev = None #kth.next
        curr = head # groupPrev.next

        while curr: #!= groupNext
            nxt= curr.next
            curr.next = prev
            prev = curr
            curr= nxt
        
        #groupPrev.next= kth
    
        '''
        #missed prev= kth.next, curr != groupNext, edge case if kth is None
        dummy =ListNode(0,head)
        groupPrev=dummy

        while True:
            kth = self.kthNode(groupPrev, k)
            if not kth:
                break
            groupNext=kth.next

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next
    
    def kthNode(self, node, k):
        while node and k>0:
            node = node.next
            k-=1
        return node
