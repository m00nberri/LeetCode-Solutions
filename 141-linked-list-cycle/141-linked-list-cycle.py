# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        hashset = set()
        node = head
        
        while node:
            if node.next in hashset:
                return True
            else:
                hashset.add(node)
                node = node.next
        
        return False