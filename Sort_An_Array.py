class Solution(object):
    # def sortArray(self, nums):
    #     for i in range(len(nums)-1):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] > nums[j]:
    #                 temp = nums[i]
    #                 nums[i] = nums[j]
    #                 nums[j] = temp
    #     return nums

    def merge(self, left, right):
        result = []
        index = 0
        l = 0
        r = 0
        print(left)
        print(right)

        # 2. compare and merge
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            # elif right[r] < left[l]:
            # when right[r] and left[l] are equal
            # only index increases
            else:
                result.append(right[r])
                r += 1
            index += 1
        
        # 3. remainder
        while l < len(left):
            result.append(left[l])
            l += 1
            index += 1
        while r < len(right):
            result.append(right[r])
            r += 1
            index += 1
        return result

    def sortArray(self, nums):
        # print(nums)
        if len(nums) == 1:
            return nums
        mid = len(nums)//2
        # left = nums[:mid]
        # right = nums[mid:]
        
        # 1. dividing / finding base case
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)

def main():
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6]
    print(sol.sortArray(nums))

if __name__ == "__main__":
    main()


# show me a shorting algorithm
# merge, quick, bubble, insertion, (heap)