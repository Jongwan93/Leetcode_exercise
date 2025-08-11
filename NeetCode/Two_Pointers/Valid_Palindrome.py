class Solution:
    def isPalindrome(self, s):
        trim_s = ''.join(c.lower() for c in s if c.isalnum()) # seq[start:stop:step]
        # trim_s = ""
        # for c in s:
        #     if c.isalunum():
        #         trim_s += c.lower()
        return trim_s == trim_s[::-1]
    # PROBLEM:
    # - uses extra memory
    # - uses built in python library
    # - interviewer might want you to do it yourself

    # - isalnum is useful!
    # def isPalindrome(self, s):
    # l, r = 0, len(s) - 1
    # isalnum = str.isalnum
    # lower = str.lower

    # while l < r:
    #     while l < r and not isalnum(s[l]):
    #         l += 1
    #     while l < r and not isalnum(s[r]):
    #         r -= 1
    #     if lower(s[l]) != lower(s[r]):
    #         return False
    #     l += 1
    #     r -= 1
    # return True      

def main():
    sol = Solution()
    s = "0P"
    print(sol.isPalindrome(s))

if __name__ == "__main__":
    main()



# https://neetcode.io/problems/is-palindrome?list=neetcode250