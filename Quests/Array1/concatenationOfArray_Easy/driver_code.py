import json
import getConcatenation

with open("test_cases.json") as f:
    data = json.load(f)

tests = data["tests"]
sol = getConcatenation.Solution()


passed = 0
for idx, t in enumerate(tests):
    nums = t["nums"]
    expected = t["expected"]

    result = sol.getConcatenation(nums)

    if result == expected:
        print(f"Test {idx + 1}: PASSED")
        passed += 1
    else:
        print(f"Test {idx + 1}: FAILED ❌")
        print(f"  Input:     {nums}")
        print(f"  Expected:  {expected}")
        print(f"  Got:       {result}")

print(f"\nPassed {passed}/{len(tests)} tests.")