class Solution:
    def removeElement(self, nums, val):        
        nums[:] = [x for x in nums if x != val]
        return len(nums)

def main():
    sol = Solution()
    nums = [1,1,2,3,4]
    val = 1
    print(sol.removeElement(nums, val))

if __name__ == "__main__":
    main()




# nums[:] = [x for x in nums if x != val]
# - make a new list that contains every element in nums that is equal to val.
# - nums[:] = update its list. so creating new list name "nums"

# x for x in nums if x != val
# -  first x: what you want to put into the new list
# -  for x in nums: for every x in nums list
# -  if x != val: x that is not equal to val