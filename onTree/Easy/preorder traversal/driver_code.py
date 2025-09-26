from build_tree import buildtree
import json
from preorderTraversal import Solution

with open("test_cases.json") as f:
    test_cases = json.load(f)

for i, case in enumerate(test_cases, 1):
    treeBuilding = buildtree(case["input"])
    sol = Solution()
    check = sol.preorderTraversal(treeBuilding)

    if check != case["expected"]:
        print("oopps. try again")
    else:
        print("hooorayyy")
