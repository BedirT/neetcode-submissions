# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = False

        last_node = None
        result_head = None
        
        while l1 or l2 or rem:
            val = 0
            if l1:
                val += l1.val 
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            if rem:
                val += 1
                rem = False
            
            if val > 9:
                rem = True
                val = val % 10
            
            cur_node = ListNode(val=val, next=None)
            if result_head is None:
                result_head = cur_node
            
            if last_node:
                last_node.next = cur_node

            last_node = cur_node

        

        return result_head
                