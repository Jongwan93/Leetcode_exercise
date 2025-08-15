class Solution:
    # def isValid(self, s):
    #     stack = []
    #     for c in s:
    #         if c == '(' or c == '{' or c == '[':
    #             stack.append(c)
    #         elif (c == ')' or c == '}' or c == ']') and not stack:
    #             return False
    #         else:
    #             a = stack.pop()
    #             if (a == '[' and c != ']') or (a == '{' and c != '}') or (a == '(' and c != ')'):
    #                 return False
    #     if stack:
    #         return False
    #     return True
    
    # Another solution using Dictionary
    def isValid(self, s):
        pairs = {
            ')': '(', 
            '}': '{', 
            ']': '['}
        stack = []
        for c in s:
            if c in pairs.values():
                stack.append(c)
            elif c in pairs:
                # need to check if s is not fully iterated but stack is empty
                # that means not all closing parenthesis have pairs
                if not stack or stack.pop() != pairs[c]:
                    return False
        return not stack
def main():
    sol = Solution()
    s = "([{}])"
    print(sol.isValid(s))

if __name__ == "__main__":
    main()


# https://neetcode.io/problems/validate-parentheses?list=neetcode250