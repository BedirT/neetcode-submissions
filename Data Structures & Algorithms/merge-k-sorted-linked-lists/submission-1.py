# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        items = []
        for idx, ls in enumerate(lists):
            if ls:
                items.append((ls.val, idx))

        heapq.heapify(items)

        head = None
        cur_node = None
        while items:
            min_value = items[0][0]
            min_list_idx = items[0][1]
            lists[min_list_idx] = lists[min_list_idx].next
            if lists[min_list_idx] is None:
                # remove completely
                heapq.heappop(items)
            else:
                heapq.heapreplace(items,(lists[min_list_idx].val, min_list_idx))
            if head is None:
                head = ListNode(min_value)
                cur_node = head
            else:
                cur_node.next = ListNode(min_value)
                cur_node = cur_node.next

        return head

        
        