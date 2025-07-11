class Solution:
    def isPalindrome(self, s):
        trim_s = ''.join(c.lower() for c in s if c.isalnum())
        # trim_s = ""
        # for c in s:
        #     if c.isalunum():
        #         trim_s += c.lower()
        return trim_s == trim_s[::-1]
    # PROBLEM:
    # - uses extra memory
    # - uses built in python library
    # - interviewer might want you to do it yourself

    
    # Another solution but very inefficient
    # def isPalindrome(self, s):
    #     l, r = 0, len(s)-1
    #     while l < r:
    #         while l < r and not self.alphaNum(s[l]):
    #             l += 1
    #         while r > l and not self.alphaNum(s[r]):
    #             r -= 1
    #         if s[l].lower() != s[r].lower():
    #             return False
    #         l, r = l+1, r-1
    #     return True     
    #
    # def alphaNum(self, c):
    #     return (ord('A') <= ord(c) <= ord('Z') or 
    #             ord('a') <= ord(c) <= ord('z') or
    #             ord('0') <= ord(c) <= ord('9'))            

def main():
    sol = Solution()
    s = "0P"
    print(sol.isPalindrome(s))

if __name__ == "__main__":
    main()