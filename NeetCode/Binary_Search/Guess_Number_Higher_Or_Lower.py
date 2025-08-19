# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n):
        low = 1
        high = n

        while low <= high:
            mid = low + (high - low) // 2

            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                high = mid - 1
            elif guess(mid) == 1:
                low = mid + 1
        
        return mid



def main():
    sol = Solution()
    n = 5
    pick = 3
    print(sol.guessNumber(n))

if __name__ == "__main__":
    main()



# https://neetcode.io/problems/guess-number-higher-or-lower?list=neetcode250