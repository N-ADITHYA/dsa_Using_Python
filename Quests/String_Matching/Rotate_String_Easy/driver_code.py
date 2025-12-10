import json
from rotateString import Solution
sol = Solution()

with open("test_cases.json") as f:
    test_cases = json.load(f)


for i, test in enumerate(test_cases["tests"]):
    input = test["input"]
    expected = test["expected"]
    output = sol.rotateString(input["s"], input["goal"])
    if output == expected:
        print("Hooray")
        print()
    else:
        print("Nope")
        print("Input is :", input["s"])
        print("Goal is: ", input["goal"])
        print(expected)