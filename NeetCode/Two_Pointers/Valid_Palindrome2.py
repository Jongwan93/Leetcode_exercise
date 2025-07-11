class Solution:
    def validPalindrome(self, s):
        ## this is Brute Force Solution
        # if s == s[::-1]:
        #     return True
        
        # elif not s == s[::-1]:
        #     for i in range(len(s)):
        #         tmp = ""
        #         tmp += s[0:i] + s[i+1:len(s)]
        #         if tmp == tmp[::-1]:
        #             return True
        # return False

        # Two pointer solution
        # - "remove at most one alphabet" means you only need to find one alphabet and try removing it.
        l, r = 0, len(s)-1
        while l<r:
            if s[l] != s[r]:
                skipl = s[l+1 : r+1]
                skipr = s[l : r]
                return skipl == skipl[::-1] or skipr == skipr[::-1]
            l+=1
            r-=1
        return True            
    
def main():
    sol = Solution()
    s = "abbda"
    print(sol.validPalindrome(s))

if __name__ == "__main__":
    main()