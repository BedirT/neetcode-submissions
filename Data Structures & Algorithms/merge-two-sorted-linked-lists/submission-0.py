# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        cur_node = None

        def increment_node(new_node: ListNode) -> None:
            nonlocal head, cur_node
            if head is None:
                # initializing head and cur_node
                head = ListNode(new_node.val)
                cur_node = head
            else:    
                cur_node.next = ListNode(new_node.val)
                cur_node = cur_node.next
            return new_node.next

        while list1 or list2:
            val1 = list1.val if list1 else None
            val2 = list2.val if list2 else None

            if val1 is None:
                list2 = increment_node(list2)
            elif val2 is None:
                list1 = increment_node(list1)
            elif val1 < val2:
                list1 = increment_node(list1)
            elif val2 < val1:
                list2 = increment_node(list2)
            else: # val1 == val2
                list1 = increment_node(list1)
                list2 = increment_node(list2)

        return head
                