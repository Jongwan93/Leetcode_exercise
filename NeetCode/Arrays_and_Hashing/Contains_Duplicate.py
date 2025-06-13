class Solution:
    def hasDuplicate(self, nums):
        myDict = dict()
        for n in nums:
            if n not in myDict:
                myDict[n] = 0
            myDict[n] += 1
            if myDict[n] > 1:
                return True
        return False
    
    # easiest one:
    # return len(set(nums)) < len(nums)
    # Woalla!!

def main():
    sol = Solution()
    nums = [1, 2, 3, 3]
    print(sol.hasDuplicate(nums))

if __name__ == "__main__":
    main()