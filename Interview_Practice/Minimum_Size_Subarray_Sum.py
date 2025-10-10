class Solution(object):
    def minSubArrayLen(self, target, nums):
        # l, r 0번째 인덱스에서 시작
        # r을 오른쪽으로 옮긴다.
        # - nums[l]~nums[r] 사이 숫자들 합이 target숫자와 같거나 커질때까지
        # sliding window length저장 (minLength)
        # l을 오른쪽으로 하나 옮김
        # - nums[l]~nums[r] 사이 숫자들 합이 target숫자보다 작아질때까지
        # 반복.
        # l > r 이된다면 멈춘다

        # l, r = 0, 0
        # subarray_sum = 0 # 변수명 잘골라야함
        # minLength = float("inf")
        # while r < len(nums):
        #     # out of boundary 신경쓰기
        #     while subarray_sum < target and r < len(nums) and nums[r+1] + subarray_sum < target:
        #         subarray_sum += nums[r]
        #         r += 1
        #     print(r)

        #     while subarray_sum >= target and l < r:
        #         if r - l + 1 < minLength:
        #             minLength = r - l + 1
        #         subarray_sum -= nums[l]
        #         l += 1
        #     print(l)
        #     r += 1
        # return minLength

        l, r = 0, 0
        subarray_sum = 0 # 변수명 잘골라야함
        minLength = float("inf")
        
        for r in range(len(nums)):
            subarray_sum += nums[r]
            
            while subarray_sum >= target:
                # if r - l + 1 < minLength:
                #     minLength = r - l + 1
                minLength = min(r - l + 1, minLength)
                subarray_sum -= nums[l]
                l += 1
        
        # if minLength == float("inf"):
        #     return 0
        return 0 if minLength == float("inf") else minLength
            
def main():
    sol = Solution()
    target = 7
    nums = [2,3,1,2,4,3]
    print(sol.minSubArrayLen(target, nums))

if __name__ == "__main__":
    main()