# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        l = head
        r = head.next
        while r and r.next:
            if l is r:
                return True
            else:
                l=l.next
                r=r.next.next
        return False