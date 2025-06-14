import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        numDict = dict()
        for n in nums:
            if n not in numDict:
                numDict[n] = 0
            numDict[n] += 1

        # nums = [1, 1, 1, 2, 2, 2, 2, 3, 5, 5, 5, 5, 5, 5]
        # 1 : 3
        # 2 : 4
        # 3 : 1
        # 4 : 0
        # 5 : 6

        # 트리 생성
        # heapify
        # min-heap
        # 배열로 써서 이거를 heap처럼 다뤄줘? (python이 할수있음)
        # heap을 왜쓰는지?
        # heap이 가지는 성질
            # min heap이라는것은 제일 적은것을 빨리 찾아낼수있도록 해주는 자료구조
            # k = 2일때, heap 사이즈가 2가 될때까지 넣는다.
            # heap의 사이즈가 2가 넘었을때 맨위 노드를 뺀다
            # heap은 사이즈를 유지한다. K개로

        result = []
        heap = []
        for num, cnt in numDict.items():
            # heapq.heappush(heap, [num, cnt])
            # python takes first element as a sorting standard
            heapq.heappush(heap, [cnt, num])
            if len(heap) > k:
                heapq.heappop(heap)
        
        # heap 이 만들어졌음 (ascending order)
        for _ in range(len(heap)):
            result.append(heapq.heappop(heap)[1])

        return result

def main():
    sol = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(sol.topKFrequent(nums, k))


if __name__ == "__main__":
    main()