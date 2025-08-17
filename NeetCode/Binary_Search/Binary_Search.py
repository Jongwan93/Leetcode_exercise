class Solution:
    def search(self, nums, target):
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
            
        return -1

def main():
    sol = Solution()
    nums = [-1,0,2,4,6,8]
    target = 4
    print(sol.search(nums, target))

if __name__ == "__main__":
    main()



# https://neetcode.io/problems/binary-search?list=neetcode250 