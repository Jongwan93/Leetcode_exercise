class Solution(object):
    def search(self, nums, target):
        # binary tree의 성질을 설명하시오
        
        # l, r
        # mid = (l + r) // 2
        # nums[mid]가 target보다 작은가 큰가
        # if nums[mid] < target
        # l = mid + 1
        # elif nums[mid] > target
        # r = mid - 1
        # else return 
        # while l < r

        l = 0
        r = len(nums)
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1