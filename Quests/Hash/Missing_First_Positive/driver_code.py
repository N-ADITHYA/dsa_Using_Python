from json import load
from firstMissingPositive import Solution

with open("test_cases.json") as f:
    test_cases = load(f)

for i, test in enumerate(test_cases):
    sol = Solution()
    inpt = test["input"][::]
    inp = inpt
    expected = test["expected"]
    output = sol.firstMissingPositive(inp)
    if output == expected:
        print("Success Buddy\n")
    else:
        print("Work hard!")
        print("Input: ", inpt)
        print("Output: ", output)
        print("Expected: ", expected,'\n')

