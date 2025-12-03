from kSmallestPairs import Solution
import json

with open("test_cases.json") as f:
    test_cases = json.load(f)

idx = 0
for data in test_cases["tests"]:
    sol = Solution()
    out = sol.kSmallestPairs(data["nums1"], data["nums2"], data["k"])

    if out == data["expected"]:
        print("Hooray")
    else:
        print("Nope")
print(test_cases["tests"])