from json import load
from detectCapitalUse import Solution

with open("test_cases.json") as f:
    test_cases = load(f)

for i, test in enumerate(test_cases["tests"]):
    sol = Solution()
    inp = sol.detectCapitalUse(test["word"])

    if inp == test["expected"]:
        print(f"Test case {i} is Passed ❤️")
        print("Input: ", test["word"])
        print("Output: ", test["expected"])
        print("Reason is ", test["reason"])
    else:
        print(f"Test case {i} is Failed 😔️")
        print("Input: ", test["word"])
        print("Output: ", test["expected"])
        print("Reason is ", test["reason"])


