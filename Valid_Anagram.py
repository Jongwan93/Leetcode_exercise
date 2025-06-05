class Solution(object):
    def isAnagram(self, s, t):
        # {}
        # {a : 3}
        # {n : 1}
        # {g : 1}
        # {r : 1}
        # {m : 1}
        if len(s) != len(t):
            return False

        charCountMap = {}
        for c in s:
            if c not in charCountMap:
                charCountMap[c] = 1
            else:
                charCountMap[c] += 1
        
        for c in t:
            if c not in charCountMap or charCountMap[c] == 0:
                return False
            charCountMap[c] -= 1
        
        if any(v > 0 for v in charCountMap.values()):
            return False
        
        return True
        
# 30 minutes total
# not brute force

# List, Set, Map
# Stack, Queue, Heap
# Tree, LinkedList, Graph

                

def main():
    sol = Solution()
    s = "anagram"
    t = "nagaram"
    print(sol.isAnagram(s, t))

if __name__ == "__main__":
    main()