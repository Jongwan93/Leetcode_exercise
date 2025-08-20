# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        current1 = list1
        current2 = list2
        sortedHead = None

        if not list1:
            return list2
        
        if not list2:
            return list1

        while current1 and current2:
            if current2.value <= current1.value:
                next2 = current2.next
                current2.next = current1
                current2 = next2
                current1 = current1.next


        
        