class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False

def main():
    sol = Solution()
    nums = [1,2,3,1]
    k = 3
    print(sol.containsNearbyDuplicate(nums, k))

if __name__ == "__main__":
    main()


# https://neetcode.io/problems/contains-duplicate-ii?list=neetcode250