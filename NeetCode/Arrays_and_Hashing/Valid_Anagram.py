class Solution:
    def isAnagram(self, s, t):
        myDict = dict()
        for c in s:
            if c not in myDict:
                myDict[c] = 0
            myDict[c] += 1
        
        for c in t:
            if c not in myDict:
                return False
            myDict[c] -= 1

        if any(value > 0 for value in myDict.values()):
            return False
        
        return True

def main():
    sol = Solution()
    s = "jar"
    t = "jam"
    print(sol.isAnagram(s, t))

if __name__ == "__main__":
    main()