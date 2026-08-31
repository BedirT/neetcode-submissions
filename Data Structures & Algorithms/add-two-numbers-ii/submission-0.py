# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def get_number(self, node) -> str:
        cum_val = ""
        if node.next:
            cum_val = self.get_number(node.next)
        return str(node.val) + cum_val

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = int(self.get_number(l1)) + int(self.get_number(l2))

        root = None
        prev = None
        for ch in str(res):
            node = ListNode(int(ch))
            if root is None:
                root = node
                prev = node
            else:
                prev.next = node
                prev = node

        return root
