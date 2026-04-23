# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        dummy = ListNode()
        dummy.next = head
        l, r = dummy, dummy
        c=0
        while r and c< n+1:
            r = r.next
            c+=1
        while r:
            l=l.next
            r=r.next
        
        l.next = l.next.next

        return dummy.next
        
        
        
        
        
