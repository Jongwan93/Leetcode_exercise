class Solution:
    def majorityElement(self, nums):
        myDict = {}
        for n in nums:
            if n not in myDict:
                myDict[n] = 0
            myDict[n] += 1
        
        majorValue = 0
        for value in myDict.values():
            if value > majorValue:
                majorValue = value
        
        majorElement = 0
        for k, v in myDict.items():
            if v == majorValue:
                majorElement = k
        
        return majorElement

def main():
    sol = Solution()
    nums = [5,5,1,1,1,5,5]
    print(sol.majorityElement(nums))

if __name__ == "__main__":
    main()


# this method is done by using dictionary
# better answer is in LeetCode file
# best answer:
# nums.sort()
# return nums[len(nums)//2]