import json
from maxSubArray import Solution


with open("test_cases.json") as f:
    test_cases = json.load(f)

for i, case in enumerate(test_cases, 1):
    result = Solution().maxSubArray(case["input"]["nums"])


    if result != case["output"]:
        print(f"ooops!, Test case {i} is failed")
        print("Input: ", case["input"])
        print("Expected: ", case["output"])
        print("Got: ", result)
        print()
    else:
        print(f"Test case {i} passed! 😎")
        print("Input: ", case["input"])
        print("Expected: ", case["output"])
        print("Got: ", result)
        print()