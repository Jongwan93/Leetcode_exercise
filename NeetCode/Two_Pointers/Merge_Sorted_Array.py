class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        nums1_copy = nums1[:m]
        idx = 0
        i = j = 0
        while idx < m + n:
            if j >= n or (i < m and nums1_copy[i] <= nums2[j]):
                nums1[idx] = nums1_copy[i]
                i += 1
            else:
                nums1[idx] = nums2[j]
                j += 1
            idx += 1


def main():
    sol = Solution()
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    print(sol.merge(nums1, m, nums2, n))
    print(nums1)

if __name__ == "__main__":
    main()

# https://neetcode.io/problems/merge-sorted-array?list=neetcode250