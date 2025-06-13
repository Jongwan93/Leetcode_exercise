class Solution(object):
    def removeDuplicates(self, nums):
        index = 1
        for i in range(len(nums)):
            if nums[i] != nums[index-1]:
                nums[index] = nums[i]
                index+=1
        return index
    
    # return condition was complicated.
    # update nums array directly and return number of total unique elements

def main():
    sol = Solution()
    nums = [1, 1, 2]
    print(sol.removeDuplicates(nums))
    print(nums)

if __name__ == "__main__":
    main()