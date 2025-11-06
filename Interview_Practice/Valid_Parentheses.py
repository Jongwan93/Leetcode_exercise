class Solution:
    def isValid(self, s: str) -> bool:
        # dictionary
        # key: ), value: (
        # key: }, value: {
        # key: ], value: [
        bracketsDict = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c not in bracketsDict:
                stack.append(c)
                # stack = ["(", "[", "{"]
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() != bracketsDict[c]:
                    return False
        return len(stack) == 0
        
def main():
    sol = Solution()
    s = "([{}])"
    print(sol.isValid(s))

if __name__ == "__main__":
    main()