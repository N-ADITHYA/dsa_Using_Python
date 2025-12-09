import json
from repeatedStringMatch import Solution
# Loading testcases
with open("test_cases.json", "r") as f:
    tests = json.load(f)

sol = Solution()

for idx, t in enumerate(tests, 1):
    a = t["a"]
    b = t["b"]
    expected = t["expected"]

    result = sol.repeatedStringMatch(a, b)
    status = "PASS" if result == expected else "FAIL"

    print(f"Test {idx}: a='{a}', b='{b}' -> Output={result}, Expected={expected} [{status}]")
