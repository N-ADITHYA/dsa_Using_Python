from overlapping import Solution
import json

with open("test_cases.json") as f:
    test_cases = json.load(f)

for i, case in enumerate(test_cases, 1):
    sol = Solution()
    result = sol.eraseOverlapIntervals(case["input"])

    if result != case["output"]:
        print(f"❌ Test case {i} failed")
        print(f"   Input: {case['input']}")
        print(f"   Expected: {case['output']}, Got: {result}")
    else:
        print(f"✅ Test case {i} passed")
