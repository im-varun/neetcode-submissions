# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        middle = (length // 2) + 1
        count = 0
        curr = head
        while curr:
            count += 1
            if count == middle:
                return curr
            
            curr = curr.next