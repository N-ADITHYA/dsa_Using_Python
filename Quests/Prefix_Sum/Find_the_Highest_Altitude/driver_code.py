from json import load
from largestAltitude import Solution

with open("test_cases.json") as f:
    test_cases = load(f)

for i, test in enumerate(test_cases):
    sol = Solution()
    inp = test["input"]["gain"]
    out = sol.largestAltitude(inp)
    expected = test["output"]
    if out == expected:
        print(f"Done, Passed test case number {i}\n")
    else:
        print("Nope")
        print("Input: ", inp)
        print("Output: ", out)
        print("Expected: ", expected)


