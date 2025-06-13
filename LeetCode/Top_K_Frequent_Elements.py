class Solution(object):
    def topKFrequent(self, nums, k):
        numDict = dict()
        for n in nums:
            if n not in numDict:
                numDict[n] = 0
            numDict[n] += 1
        # 1 : 3
        # 2 : 2
        # 3 : 1
        arr = []
        for num, cnt in numDict.items():
            arr.append([cnt, num])
        arr.sort(reverse=True)

        result = []
        for i in range(0, k):
            result.append(arr[i][1])
        
        return result

def main():
    sol = Solution()
    nums = [4,1,-1,2,-1,2,3]
    k = 2
    print(sol.topKFrequent(nums, k))

if __name__ == "__main__":
    main()



# O(1) > O(logN) > O(N) > O(NlogN) > O(N^2)