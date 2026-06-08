# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        traversing entire linked lists- adding to array
        then summing arrays 
        arr1=[]
        while l1:
            arr.append(l1.next)
            l1 = l1.next
        arr2=[]
        while l2:
            arr.append(l2.next)
            l2 = l2.next
        

        '''

        dummy = ListNode()
        cur = dummy

        carry=0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #addthenumbers
            val = v1 + v2 + carry
            carry = val//10
            val = val%10
            cur.next = ListNode(val)

            #update the pointers
            cur = cur.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
            
        return dummy.next



        