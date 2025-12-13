import json
from twoSum import Solution

with open("test_cases.json") as f:
    test_cases = json.load(f)

sol = Solution()
for i, case in enumerate(test_cases, 1):
    result = sol.two_sum(**case["input"])
    ans = 0
    for i in result:
        ans += case["input"]["nums"][i]
    answer = (ans == case["input"]["target"])
    if not answer:
        print("Failed Test Case😔")
        print("Input:", case["input"])
        print("Expected:", case["output"])
        print("Got:", result)
        print()
    else:
        print("Expected: ", case["output"])
        print("Got: ", result)
        print("Test case passed😎")
        print()
