# Done
def isPalindrome(self, num):
    reversedNum = 0
    temp = num
    if num < 0:
        return False
    while temp > 0:
        # key line
        reversedNum = reversedNum * 10 + (temp % 10)
        temp //= 10
    if reversedNum == num:
        return True
    return False

# this way is reversing the int num.
# other way:
# - you can compare digits from both ends
