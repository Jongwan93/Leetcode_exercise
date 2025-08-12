class Solution:
    def removeDuplicates(self, nums):
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
        return l
            
def main():
    sol = Solution()
    nums = [1,1,2,3,4]
    print(sol.removeDuplicates(nums))
    print(nums)

if __name__ == "__main__":
    main()


# https://neetcode.io/problems/remove-duplicates-from-sorted-array?list=neetcode250