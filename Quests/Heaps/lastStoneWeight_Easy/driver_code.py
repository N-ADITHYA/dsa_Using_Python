import json
from lastStoneWeight import Solution

with open("test_cases.json") as f:
    test_cases = json.load(f)


for t in test_cases["tests"]:
    stones = t["stones"]
    sol = Solution()
    if sol.lastStoneWeight(stones) != t["expected"]:
        print()
        print("OOPS, Failed Bro")
        print("Input: ", t["stones"])
        print("Expected: ", t["expected"])
        print("Output: ", sol.lastStoneWeight(stones))
    else:
        print()
        print("Hoorayyyy")
        print("Input: ", t["stones"])
        print("Output: ", sol.lastStoneWeight(stones))
        print("Expected: ", t["expected"])

