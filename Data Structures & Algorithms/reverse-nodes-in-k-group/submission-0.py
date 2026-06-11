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
        dummy = ListNode(0,head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext= kth.next

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr =tmp

            #groupPrev move
            tmp = groupPrev.next #tmp =1
            groupPrev.next = kth # dummy points at three
            groupPrev = tmp #since temp = 1
            
        return dummy.next


    def getKth(self, curr, k):
        while curr and k >0:
            curr = curr.next
            k-=1
        return curr 


