import json
from shuffle import Solution
with open("test_cases.json") as f:
    data = json.load(f)

sol = Solution()

for i, t in enumerate(data["tests"], 1):
    nums, n, expected = t["nums"], t["n"], t["expected"]
    out = sol.shuffle(nums, n)
    print(f"Test {i}: {'PASS' if out == expected else 'FAIL'} | Output={out}")
