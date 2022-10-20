# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        previous = None
        current = head
        
        while current != None:
            mem = current.next
            current.next = previous
            previous = current
            current = mem
        
        return previous

    
    
#solved after viewing neetcode solution