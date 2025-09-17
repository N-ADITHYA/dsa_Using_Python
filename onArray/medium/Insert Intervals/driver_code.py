from insert import Solution
import json

with open("test_cases.json") as f:
    test_cases = json.load(f)


for i, case in enumerate(test_cases, 1):
    sol = Solution()
    result = sol.insert(case["input"]["intervals"], case["input"]["newInterval"])

    if result != case["output"]:
        print("Oh ohhh, Its wrong")
        print("Input: ", case["input"])
        print("newInterval: ", case["input"]["newInterval"])
        print("Expected: ", case["output"])
        print()
    else:
        print("Oh Yeahhh, It's Righttt! 😎")
        print("Input: ", case["input"])
        print("newInterval: ", case["input"]["newInterval"])
        print("Expected: ", case["output"])
        print()
