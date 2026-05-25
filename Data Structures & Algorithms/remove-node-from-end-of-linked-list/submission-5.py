# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        l,r = head, head

        for i in range(n-1):
            r = r.next
        
        prev = None
        while r.next is not None:
            print(l.val, r.val)
            prev = l
            l = l.next
            r = r.next
        
        if prev is None:
            return l.next
        
        else:
            prev.next = l.next
            return head

        