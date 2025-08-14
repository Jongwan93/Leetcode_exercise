class Solution:
    def maxProfit(self, prices):
        # date = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i + 1, len(prices)):
        #         sell  = prices[j]
        #         date = max(date, sell - buy)
        # return date

        l, r = 0, 1
        maxPrice = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxPrice = max(maxPrice, profit)
            else:
                l = r
            r += 1
        return maxPrice

def main():
    sol = Solution()
    prices = [10,1,5,6,7,1]
    print(sol.maxProfit(prices))

if __name__ == "__main__":
    main()


# https://neetcode.io/problems/buy-and-sell-crypto?list=neetcode250
