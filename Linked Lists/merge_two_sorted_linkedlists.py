# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        res_node = ListNode(0)
        head = res_node
        
        while l1 and l2:
            if l1.val < l2.val:
                res_node.next = l1
                l1 = l1.next
                
            else:
                res_node.next = l2
                l2 = l2.next
                
            res_node = res_node.next
                
        if l1 is not None:
            res_node.next = l1
            
        if l2 is not None:
            res_node.next = l2
            
        return head.next
                
                
                
        