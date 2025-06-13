class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        resultHead = ListNode()
        result = resultHead
        
        while list1 or list2:
            if not list1:
                result.next = list2
                break
            elif not list2:
                result.next = list1
                break
            elif list2.val <= list1.val:
                result.next = list2
                list2 = list2.next
            elif list1.val <= list2.val:
                result.next = list1
                list1 = list1.next
            result = result.next
        return resultHead.next
    
    # result = list1 or list2
    # if list1 or list2 is empty, just connect the result.next to remainder list.

def main():
    sol = Solution()
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    sol.mergeTwoLists(list1, list2)

if __name__ == "__main__":
    main()