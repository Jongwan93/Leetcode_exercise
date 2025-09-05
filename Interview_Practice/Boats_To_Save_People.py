class Solution:
    def numRescueBoats(self, people, limit):
        # 리스트에 최소 두명이 남을때까지만 체크하면 됨
        # 두명이 남으면 카운트 +=1 하고 리턴
            # people = [5,1,4,2], limit = 6
        # sortedPeople = [1, 2, 4, 5, 5]
        
        # 왼쪽 오른쪽 포인터 두개 만들기
        l = 0
        r = len(people)-1
        
        # people array를 sort한다
        people.sort()
        
        # while 하나필요함 조건: l<r
        # people[l] + people[r] <= 6인지 확인
        # 맞다: l+=1 r-=1
        # 아니다: r-=1
        # count+=1
        # return count
        count = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            count += 1
        return count



# https://neetcode.io/problems/boats-to-save-people?list=neetcode250