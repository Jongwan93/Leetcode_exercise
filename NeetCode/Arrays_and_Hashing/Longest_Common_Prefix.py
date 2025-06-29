# pass
def findLongestPrefix(strs):
    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

def main():
    strs = ["dance","dag","danger","damage"]
    print(findLongestPrefix(strs))

if __name__=="__main__":
    main()



# talk while thinking
# implement while thinking
# how are you going to solve it?
# - give me some time to think about it (2-3 mins)
# time/space complexity
# different solution
# don't spend more than 5 minutes to think about the solution.
# - even if its a brute force solution.
# - explain the improved solution
