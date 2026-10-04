# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        node = head
        while node:
            if node in visited:
                return True
            visited.add(node)
            node = node.next

        return False