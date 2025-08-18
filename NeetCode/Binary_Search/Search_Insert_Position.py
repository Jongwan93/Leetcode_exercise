class Solution:
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        return low

def main():
    sol = Solution()
    nums = [-1,0,2,4,6,8]
    target = 10
    print(sol.searchInsert(nums, target))

if __name__ == "__main__":
    main()



# https://neetcode.io/problems/search-insert-position?list=neetcode250 