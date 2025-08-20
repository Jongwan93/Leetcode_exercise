# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# how to append SinglyLinkedList()
# class SingleyLinkedList():
#     def __init__(self):
#         self.head = None
    
#     def append(self, val):
#         node = ListNode(val)
#         if self.head is None:
#             self.head = node
#             return
        
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = node

class Solution:
    def reverseList(self, head):
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
        

def main():
    sol = Solution()
    head = [0,1,2,3]
    print()

if __name__ == "__main__":
    main()





# https://neetcode.io/problems/reverse-a-linked-list?list=neetcode250