# pass
def majorityElement(nums):
    count = 0
    majorNumber = None

    for num in nums:
        if count == 0:
            majorNumber = num
        if majorNumber == num:
            count += 1
        else:
            count -= 1
    return majorNumber

# 중간에 생각하는과정에서 공백이 너무길다.
# 좀더 설명을 하면서 하던지 해야할듯
# 길어야 3분을 안넘게