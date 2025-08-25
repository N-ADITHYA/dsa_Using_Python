# Driver code to run the maxProfit.py
# Showcases results based on the input from test_cases.json


import json
from maxProfit import Solution

with open("test_cases.json") as f:
    test_cases = json.load(f)

for i, case in enumerate(test_cases, 1):
    result = Solution().maxProfit(**case["input"])
    if result != case["output"]:
        print("Failed Test Case😔")
        print("Input: ", case["input"])
        print("Expected: ", case["output"])
        print("Got: ", result)
        print()
    else:
        print("Test case passed😎")
        print("Input: ", case["input"])
        print("Expected: ", case["output"])
        print("Got: ", result)
        print()

