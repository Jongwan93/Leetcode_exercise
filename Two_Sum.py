class Solution(object):
    # def twoSum(self, nums, target):
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if (nums[i] + nums[j] == target):
    #                 return [i, j]

    # def twoSum(self, nums, target):
    #     dict = {}
    #     for i, num in enumerate(nums):
    #         diff = target - num
    #         if diff not in dict:
    #             dict.update({diff : i})
    #         else:
    #             value = dict[diff]
    #             return [i, value]
    #         print(dict) 
    # 
    # This approach is incorrect because we're saving the *needed* value (diff) as the key
    # instead of the actual numbers we've "already seen".
    # This can cause wrong indices or missed matches, since we only want to check if we've
    # seen the "pair" number before and store num: index, not diff: index.
    # The correct approach is: store dict[num] = i and check if (target - num) is in dict.

    def twoSum(self, nums, target):
        dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dict:
                value = dict[diff]
                return [value, i]
            dict[num] = i

    # answer was in dictionary.
    # subtract num from target and store it in dictionary as a key
    # num : index 

def main():
    sol = Solution()
    nums = [1, 9, 3, 5, 4, 2]
    target = 11
    print(sol.twoSum(nums, target))

if __name__ == "__main__":
    main()