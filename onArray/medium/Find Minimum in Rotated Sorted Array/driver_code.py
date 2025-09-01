from findMin import Solution
import json

with open("test_cases.json") as f:
    test_cases = json.load(f)


for i, case in enumerate(test_cases, 1):
    result = Solution().findMin(case["input"]["arr"])
    if result != case["output"]:
        print("Oh noooo, It's failed 😔")
        print("Input: ", case["input"]["arr"])
        print("Expected: ", case["output"])
        print("Got: ", result)
        print()
    else:
        print("Oh Yeahhhh, It's passed 😎")
        print("Input: ", case["input"]["arr"])
        print("Expected: ", case["output"])
        print("Got: ", result)
        print()