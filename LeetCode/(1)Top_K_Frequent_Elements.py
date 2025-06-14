class Solution(object):
    def topKFrequent(self, nums, k):
        numDict = dict()
        for n in nums:
            if n not in numDict:
                numDict[n] = 0
            numDict[n] += 1
        
        # nums = [1, 1, 1, 2, 2, 2, 2, 3]
        # 1 : 3
        # 2 : 4
        # 3 : 1

        # arr = []
        # for num, cnt in numDict.items():
        #     arr.append([cnt, num])
        # arr.sort(reverse=True)        

        # result = []
        # for i in range(0, k):
        #     result.append(arr[i][1])
        
        # return result

        # bucket sort.
        # 각 bucket마다 정해진 규칙이 있음.
        # 조건: 제일 많이 발생한 element 반환
        # 각각 몇번 발생했는가의 조건으로 
        
        # bucket을 count개수 별로 만든다
        # nums에 있는 숫자들 개수에 맞춰서 bucket에 넣는다
        # 가장 갯수를 기록한 숫자를 k개 찾는다
            # buckets를 iterate해서 
            # bucket의 맨뒤부터 돌아서 
            # list가 존재하면 result어레이 길이가 
            # k개가 될때까지 숫자를 넣어줌

        buckets = [[] for _ in range(len(nums))]
        for num, cnt in numDict.items():
            buckets[cnt-1].append(num)

        result = []
        # for i in range(len(buckets)-1, 0, -1):
        # 이렇게하면 안됨. 왜냐면 "0"이 끝이면 loop에 포함되지않음.
        for i in range(len(buckets)-1, -1, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result

def main():
    sol = Solution()
    nums = [1]
    k = 1
    print(sol.topKFrequent(nums, k))

if __name__ == "__main__":
    main()



# O(1) > O(logN) > O(N) > O(NlogN) > O(N^2)