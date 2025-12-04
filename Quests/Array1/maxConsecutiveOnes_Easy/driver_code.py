from typing import List
import json
from findMaxConsecutiveOnes import Solution
# Load testcases
with open("test_cases.json") as f:
    data = json.load(f)

sol = Solution()

for idx, t in enumerate(data["tests"], 1):
    nums = t["nums"]
    expected = t["expected"]
    output = sol.findMaxConsecutiveOnes(nums)

    status = "PASS" if output == expected else "FAIL"
    print(f"Test {idx}: {status} | Output={output} | Expected={expected}")
