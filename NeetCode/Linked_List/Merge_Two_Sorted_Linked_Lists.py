# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        dummy = ListNode(0)
        # tail will iterate through new list
        # dummy must stay pointing at first node
        tail = dummy

        # regardless of list1 and list2 structure,
        # simply compare the two nodes and connect the node with smaller value.
        while list1 and list2:
            if list2.val <= list1.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next
        
        # if list1 and list2 is not fully iterated, connect it to the tail
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next
                

# https://neetcode.io/problems/merge-two-sorted-linked-lists?list=neetcode250


        
        