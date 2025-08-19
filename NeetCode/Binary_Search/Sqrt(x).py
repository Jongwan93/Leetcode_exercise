class Solution:
    def mySqrt(self, x):
        low = 0
        high = x
        res = 0

        while low <= high:
            mid = low + (high - low) // 2

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1
            elif mid * mid < x:
                low = mid + 1
                res = mid
        return res
                


def main():
    sol = Solution()
    x = 9
    print(sol.mySqrt(x))

if __name__ == "__main__":
    main()



# https://neetcode.io/problems/sqrtx?list=neetcode250