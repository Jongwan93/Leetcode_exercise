class Solution:
    def asteroidCollision(self, asteroids):
        # for loop으로 asteroids를 돈다
        # i in asteroids
        # i > 0 이면 result에 넣어
        # i < 0 이면 result.pop()해서
        # i*-1 == result.pop() result에 다시안넣어.
        # i*-1 > result.pop()
            # result.pop()이 i*-1보다 클때까지 뽑아 and len(result) > 0
            # 그러고 마지막으로 뽑은, 그러니까 i*-1보다 큰 숫자를 result에 넣는다.
        
            
        # result의 끝이 마이너스면 asteroid를 추가해주면 된다.
        # if len(result) == 0 or result[-1] < 0:
        #     result.append(asteroid)
        #     continue
        
        # # 여기 들어온이상 result의 length는 0보다 크다. (asteroid가 존재)
        # # result의 마지막에 들어있는애는 양수다.
        # lastAsteroid = result.pop()
        # print(result)
        # while lastAsteroid < abs(asteroid) and len(result) > 0 and result[-1] > 0:
        #     lastAsteroid = result.pop()
        # if len(result) == 0:
        #     result.append(asteroid)
        # else: 
        #     result.append(lastAsteroid)

        result = []
        for a in asteroids:
            while result and result[-1] > 0 and a < 0:
                diff = a + result[-1]
                if diff > 0:
                    a = 0
                elif diff < 0:
                    result.pop()
                else:
                    a = 0
                    result.pop()
            if a:
                result.append(a)
        return result


        


def main():
    sol = Solution()
    asteroids = [2,4,-4,-1]
    print(sol.asteroidCollision(asteroids))

if __name__ == "__main__":
    main()