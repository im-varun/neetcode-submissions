# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        remove_index = length - n
        if remove_index == 0:
            head = head.next
            return head

        count = 0
        prev, curr = None, head
        while curr:
            if count == remove_index:
                prev.next = curr.next
                return head

            count += 1
            prev = curr
            curr = curr.next