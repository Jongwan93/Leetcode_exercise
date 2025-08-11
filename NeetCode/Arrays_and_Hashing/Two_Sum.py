class Solution:
    def twoSum(self, nums, target):
        myDict = dict()
        for i, num in enumerate(nums):
            other = target - num
            print(f"num print: {num}")
            print(f"other print: {other}")
            if other in myDict:
                return [myDict[other], i]
            myDict[num] = i

def main():
    sol = Solution()
    nums = [3, 4, 5, 6]
    target = 7
    print(sol.twoSum(nums, target))

if __name__ == "__main__":
    main()



# https://neetcode.io/problems/two-integer-sum?list=neetcode250