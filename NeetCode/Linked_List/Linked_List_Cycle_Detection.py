# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head):
        if head is None:
            return False
        
        list = []
        current = head
        while current:
            if current not in list:
                list.append(current)
                current = current.next
            else:
                return True
        
        return False





# https://neetcode.io/problems/linked-list-cycle-detection?list=neetcode250 