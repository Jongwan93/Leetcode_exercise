# not completed
def createPermutation(nums, path=[], result = None):
    if result is None:
        result = []

    if not nums:
        result.append(path)
        return
    
    for i in range(len(nums)):
        createPermutation(nums[:i] + nums[i+1:], path + [nums[i]], result)
    
    return result

def findNextPermutation(permutation, nums):
    for i in range(len(permutation)):
        if i == len(permutation) - 1:
            return permutation[0]
        elif permutation[i] == nums:
            return permutation[i+1]
        
def main():
    nums = [1, 1, 5]
    permutation = createPermutation(nums)
    print(permutation)
    findNums= [3, 2, 1]
    nextPermutation = findNextPermutation(permutation, findNums)
    print(nextPermutation)


if __name__ == "__main__":
    main()