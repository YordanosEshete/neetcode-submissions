# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        left = head.next
        right = head
        
        while left != None:
            if left == None or left.next == None or left.next.next == None:
                return False
            left = left.next.next
            right = right.next
            if left == right:
                return True
        return False
            
        