import json
from isPossible import Solution


with open("test_cases.json") as f:
    test_cases = json.load(f)

for i, test in enumerate(test_cases["tests"]):
    sol = Solution()
    input = sol.isPossible(test["target"])
    if input == test["expected"]:
        print(f"Test case {i} is passed 😎")
        print("Input is :", test["target"])
        print("Output is : ", test["expected"])
        print(input)
    else:
        print(f"Test case {i} is failed 😔")
        print("Input is :", test["target"])
        print("Output is : ", test["expected"])
        print(input)
