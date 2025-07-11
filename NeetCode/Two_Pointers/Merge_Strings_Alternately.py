from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # index1 = 0
        # index2 = 0
        # result = ""
        
        # while index1 < len(word1) and index2 < len(word2):
        #     result += word1[index1]
        #     result += word2[index2]
        #     index1 += 1
        #     index2 += 1
        
        # if index1 == len(word1) and index2 < len(word2):
        #     result += word2[index2:]
        # elif index2 == len(word2) and index1 < len(word1):
        #     result += word1[index1:]
        
        # return result
    
        result = []
        for a, b in zip_longest(word1, word2, fillvalue=''):
            # zip
            # word1 = "ab", word2 = "abbxxc"
            # a | a
            # b | b
            # ''| b
            # ''| x
            # ''| x
            # ''| c
            result.append(a)
            result.append(b)
        return ''.join(result)
        
def main():
    sol = Solution()
    word1 = "ab"
    word2 = "abbxxc"
    print(sol.mergeAlternately(word1, word2))

if __name__ == "__main__":
    main()