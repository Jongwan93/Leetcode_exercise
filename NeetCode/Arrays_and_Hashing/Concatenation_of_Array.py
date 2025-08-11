class Solution:
    def getConcatenation(self, nums):
        ans = []
        for i in range(0, len(nums)*2):
            ans.append(nums[i%len(nums)])
        return ans

def main():
    sol = Solution()
    nums = [1, 4, 1, 2]
    print(sol.getConcatenation(nums))

if __name__ == "__main__":
    main()



# https://neetcode.io/problems/concatenation-of-array?list=neetcode250