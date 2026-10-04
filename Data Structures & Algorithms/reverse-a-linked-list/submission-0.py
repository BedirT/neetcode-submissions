# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        bef = None
        move_to = head
        while head:
            move_to = head.next
            head.next = bef
            bef = head
            print(head.val)
            if not move_to:
                break
            head = move_to
        return head
