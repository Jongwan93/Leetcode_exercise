class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # l, r 0번째 인덱스에서 시작
        # r을 오른쪽으로 옮긴다
        # - s[l] != s[r]일때마다 k-=1 (count = k)
        # - count가 -1이 될때까지 r을 옮긴다
        # "AABA"
        # - dictionary로 알파벳들 갯수확인
        # - dictionary안에 알파벳중 제일 많은갯수를 max_count에 업데이트
        # length_of_window > k + max_count가 충족될때까지 l을 옮긴다
        # maxLength update (while끝났을때 하던지)

        l = 0
        dict = {}
        maxLength = 0 

        # dict[s[r]] = dict.get(s[r], 0) + 1
        for r in range(len(s)):
            if s[r] not in dict:
                dict[s[r]] = 0
            dict[s[r]] += 1

            # for _, v in dict.items():
            #     if max_count < v:
            #         max_count = v
            while r-l+1 > k+max(dict.values()):
                dict[s[l]] -= 1
                l += 1
            
            if maxLength < r-l+1:
                maxLength = r-l+1

        return maxLength


            


        