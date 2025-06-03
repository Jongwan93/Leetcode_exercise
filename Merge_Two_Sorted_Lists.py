class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = list1
        if not list1 and not list2:
            return None
        current = list2
        while list2.next:
            if current.val <= list1.val:
                current = list2.next
                list2.next = list1.next
                list1.next = list2
            else:
                list1 = list1.next
                list2 = list2.next
                current = current.next
        return head
                        
            

def main():
    sol = Solution()
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    sol.mergeTwoLists(list1, list2)

if __name__ == "__main__":
    main()