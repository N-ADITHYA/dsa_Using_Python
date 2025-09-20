import json
from maxPower import Solution  # make sure your maxPower class is in solution.py

with open("test_cases.json") as f:
    test_cases = json.load(f)

sol = Solution()
for i, case in enumerate(test_cases, 1):

    result = sol.maxPower(**case["input"])
    expected = case["output"]
    if result != expected:
        print("Failed Test Case😔")
        print("Input:", case["input"])
        print("Expected:", expected)
        print("Got:", result)
        print()
    else:
        print("Expected:", expected)
        print("Got:", result)
        print("Test case passed😎")
        print()
