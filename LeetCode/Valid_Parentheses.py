# DONE, try to do this again from scratch
# class Solution(object):
#     def isValid(self, s):
#         result = False
#         stack = []
#         for i in range(len(s)):
#             if not stack and s[i] not in ('(', '{', '['):
#                 return False
#             elif s[i] in ('(', '{', '['):
#                 stack.append(s[i])
#             else:
#                 top = stack.pop()
#                 if ((top == '(' and s[i] != ')') or
#                     (top == '[' and s[i] != ']') or
#                     (top == '{' and s[i] != '}')):
#                     return False
#                 else:
#                     result = True
#         if stack:
#             result = False            
#         return result

class Solution(object):
    def isValid(self, s):
        parentheses = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        stack = []
        for c in s:
            if c in parentheses.keys():
                stack.append(c)
            else:
                if not stack or parentheses[stack.pop()] != c:
                    return False
        return not stack

# couldn't think of Dictionary. 
# 1. if c in s is equal to keys(open bracket), put it in stack.
# 2. if c in s is not equal to keys(close bracket), pop a element in stack(open bracket) and compare.
# 3. stack.pop() will be used as a key in parentheses library search
# 4. also need to check if stack is empty (False)
#       - this means that s contains closing bracket only
#       - or empty S is passed
# 5. return not stack covers all the other possibilities
#       - if stack is empty(True), all brackets are paired
#       - if stack is not empty(False), it is not in pair

def main():
    sol = Solution()
    print(sol.isValid("([])"))

if __name__ == "__main__":
    main()