class Solution:
    def threeSum(self, nums):
        # nums.sort() # O(nlogn)
        
        # result = set()
        # l = 0
        # r = len(nums)-1


        # while l < r-1:
        #     mid = l+(r-l)//2
        #     while mid > l and mid < r:
        #         if nums[l] + nums[mid] + nums[r] == 0:
        #             result.add((nums[l], nums[mid], nums[r]))
        #             break
        #         elif nums[l] + nums[mid] + nums[r] < 0:
        #             while mid < r and nums[mid] != nums[mid+1]:
        #                 mid += 1
        #         else:
        #             while mid > l and nums[mid] != nums[mid-1]:
        #                 mid -= 1
        #     if l == mid:
        #         l += 1
        #     elif r == mid:
        #         r -= 1
        #     else:

        res = []
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]
        # -4에 포인터 하나 두고
        # nums[l] = -1
        # nums[r] = 2

        # -1에 포인터 하나 두고
        # nums[l] = -1
        # nums[r] = 2

        # -1에 포인터 하나 두고
        # nums[l] = 0
        # nums[r] = 2

        # 0에 포인터 하나 두고
        # nums[l] = 1
        # nums[r] = 2

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
               
                            


def main():
    sol = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(sol.threeSum(nums))

if __name__ == "__main__":
    main()