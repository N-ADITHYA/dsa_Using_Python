from minSubarray import Solution
import json
with open("test_cases.json") as f:
    test_cases = json.load(f)
print(test_cases)
for test in test_cases:
    inp = test["nums"]
    p = test["p"]
    expected = test["expected"]
    sol = Solution()
    output = sol.minSubarray(inp, p)

    if output == expected:
        print("Done")
    else:
        print("Nope")
        print("Input is: ", inp)
        print("Output is: ", output)
        print("Expected is: ", expected)