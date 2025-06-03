# DONE. Try to re do this in Leetcode from scratch
# class Solution:
#     def romanToInt(self, s):
#         roman_Symbol = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000,
#         }
        
#         result = 0
#         i = 0
#         while i < len(s)-1:
#             if roman_Symbol[s[i]] < roman_Symbol[s[i+1]]:
#                 result += roman_Symbol[s[i+1]] - roman_Symbol[s[i]]
#                 i += 2
#                 if i > len(s)-1:
#                     return result
#             else:
#                 result += roman_Symbol[s[i]]
#                 i += 1
#         result += roman_Symbol[s[len(s)-1]]
#         return result

# def main():
#     sol = Solution()
#     print(f"=={sol.romanToInt('MCMXCIV')}==")

# if __name__ == "__main__":
#     main()


# better answer:
class Solution:
    def romanToInt(self, s):
        roman_Symbol = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        result = 0
        prev = 0
        for c in reversed(s):
            curr = roman_Symbol[c]
            print(f"roman symbole: {roman_Symbol[c]}")
            if curr < prev:
                result -= curr
            else:
                result += curr
            prev = curr
            print(result)
        return result
    # so... converting roman symbol into integer is better if you do it in reverse way
    # 1. add the first index in result
    # 2. if current symbol is smaller then previous one, subtract it from result.
    #       ex) result = 5
    #           current = 1
    #           result < current
    #                5 < 1
    #           result = 4
    # this is possible because roman symbol is written largest to smallest from left to right.
    # only 'I', 'X', 'C' can come before other numbers (6 possible ways)
    #   ex) IV = 4, XC = 90, CM = 900
    #   ex) IX = 9, XL = 40, CD = 400
    # 
    # Execution Example:
    # roman symbole: 5
    # 5
    # roman symbole: 1
    # 4
    # roman symbole: 100
    # 104
    # roman symbole: 10
    # 94
    # roman symbole: 1000
    # 1094
    # roman symbole: 100
    # 994
    # roman symbole: 1000
    # 1994

def main():
    sol = Solution()
    print(f"=={sol.romanToInt('MCMXCIV')}==")

if __name__ == "__main__":
    main()