# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #so we want to remove nth node from last
        '''
         add to array
         then get the index of num to remove
         then nodes[index-1].next = nodes[index].next
         nodex = []
         curr = head
         while curr:
            nodes.append(curr)
            curr = curr.next
        
        index = len(nodes)-n
        if index ==0:
            return head.next
        
        nodex[index-1].next = nodes[index].next
        O(N) time and O(N) space array
        '''

        #O(N) time and O(1) space

        dummy = ListNode(0, head)
        l=dummy
        r= head

        #keep l and r- n spaces away
        while n >0 and r:
            r = r.next
            n-=1
    
        #move l and r to isolate the node to remove. so l will be one node before remove and r will be at the end
        
        while r:
            l= l.next
            r = r.next
        
        l.next  = l.next.next

        return dummy.next


        

        


