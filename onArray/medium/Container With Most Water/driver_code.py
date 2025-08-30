from maxArea import Solution
import json

with open("test_cases.json") as f:
    test_cases = json.load(f)

for i, case in enumerate(test_cases, 1):
    result = Solution().maxArea(case["input"]["height"])
    if result != case["output"]:
        print("Failed Test case 😔")
        print("Input: ", case["input"])
        print("Expected: ", case["output"])
        print("Got: ", result)
        print()
    else:
        print("Test case passed! 😎")
        print("Input: ", case["input"])
        print("Expected: ", case["output"])
        print("Got: ", result)
        print()