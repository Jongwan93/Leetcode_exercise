class Solution:
    # o(n) space solution because use of another stack list.
    # def reverseString(self, s):
    #     stack = []
    #     for i in range(len(s)):
    #         stack.append(s[i])
        
    #     s.clear()
    #     while stack:
    #         s.append(stack.pop())
    
    # o(1) space solution
    # def reverseString(self, s):
    #     l, r = 0, len(s)-1
    #     while l < r:
    #         s[l], s[r] = s[r], s[l]
    #         l, r = l + 1, r - 1

    # recursive solution
    # time: O(n), space: O(n) -> unefficient
    def reverseString(self, s):
        def reverse(l, r):
            if l<r:
                s[l], s[r] = s[r], s[l]
                reverse(l+1, r-1)
        reverse(0, len(s)-1)
        
def main():
    sol = Solution()
    s = ["n","e","e","t"]
    sol.reverseString(s)
    print(s)

if __name__ == "__main__":
    main()