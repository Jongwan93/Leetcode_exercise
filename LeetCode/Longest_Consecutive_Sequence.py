class Solution(object):
    def longestConsecutive(self, nums):        
        temp_Set = set(nums)

        if len(temp_Set) <= 1:
            return len(temp_Set)
        
        # count = 1 -> don't need to initialize it here
        longest = 1

        for n in temp_Set:
            if n-1 not in temp_Set:
                count = 1
                while n + count in temp_Set:
                    count += 1
                    # checking very loop? -> pointless
                    # if count > longest:
                    #     longest = count
                if count > longest:
                    longest = count
        return longest

def main():
    sol = Solution()
    nums = [100,4,200,1,3,2, 100, 4]
    print(sol.longestConsecutive(nums))

if __name__ == "__main__":
    main()


# set removes duplicating elements even if it already exists in list