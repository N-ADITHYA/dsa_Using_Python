from searchRange import Solution
import json

with open("test_cases.json") as f:
    test_cases = json.load(f)


for i, case in enumerate(test_cases, 1):
    result = Solution().searchRange(case["input"]["nums"], case["input"]["target"])
    if result != case["output"]:
        print("Oh noooo, It's failed 😔")
        print("Input: ", case["input"]["nums"])
        print("Target: ", case["input"]["target"])
        print("Expected: ", case["output"])
        print("Got: ", result)
        print()
    else:
        print("Oh Yeahhhh, It's passed 😎")
        print("Input: ", case["input"]["nums"])
        print("Target: ", case["input"]["target"])
        print("Expected: ", case["output"])
        print("Got: ", result)
        print()