import json
from licenseKeyFormatting import Solution

sol = Solution()
with open("test_cases.json") as f:
    test_cases = json.load(f)

for i, test in enumerate(test_cases):
    input = test["s"]
    if sol.licenseKeyFormatting(input, test["k"]) == test["expected"]:
        print("Hurray!")
        print("Passed Bro")
        print()
    else:
        print("Nope")
        print("Take info")
        print("Input: ", input)
        print("Output: ", sol.licenseKeyFormatting(input, test["k"]))
        print("Expected: ", test["expected"])
        print()