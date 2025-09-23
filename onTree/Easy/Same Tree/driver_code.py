import json
from build_tree import build_tree
from same_tree import Solution

def run_tests():
    with open("test_cases.json", "r") as f:
        test_cases = json.load(f)

    sol = Solution()

    for i, case in enumerate(test_cases, 1):
        p = build_tree(case["p"])
        q = build_tree(case["q"])
        result = sol.isSameTree(p, q)
        print(f"Test Case {i}: Expected={case['expected']} | Got={result} | {'✅' if result == case['expected'] else '❌'}")

if __name__ == "__main__":
    run_tests()
