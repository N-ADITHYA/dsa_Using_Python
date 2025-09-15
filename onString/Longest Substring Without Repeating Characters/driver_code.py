import json
from lengthOfLongestSubstring import Solution

# Load test cases
with open("test_cases.json") as f:
    test_cases = json.load(f)

# Create solution instance
solver = Solution()

# Run tests
for i, test in enumerate(test_cases, 1):
    result = solver.lengthOfLongestSubstring(test["input"])
    status = "✅ Passed" if result == test["expected"] else f"❌ Failed (Got {result})"
    print(f"Test Case {i}: Input={test['input']} | Expected={test['expected']} | Result={result} => {status}")
