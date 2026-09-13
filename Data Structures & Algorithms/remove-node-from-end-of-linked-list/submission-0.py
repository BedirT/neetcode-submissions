# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def traverse(node):
            if not node.next:
                order = 1
            else:
                order = 1 + traverse(node.next)

            if order == n + 1:
                # remove the child item
                node.next = node.next.next
            
            return order

        if n == traverse(head):
            if head.next:
                return head.next
            return None
        return head