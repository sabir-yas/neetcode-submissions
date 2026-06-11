# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #getting the middle node
        slow, fast = head, head.next
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
        
        second = slow.next
        slow.next=prev= None
        #reversing second half
        while second:
            tmp = second.next
            second.next = prev
            prev= second
            second= tmp
        
        first=head
        second=prev
        #merging both lists
        while second:
            tmp1,tmp2 = first.next, second.next
            first.next, second.next = second, tmp1
            first, second = tmp1, tmp2
            

