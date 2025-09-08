from minMax import Solution
import json

with open("test_cases.json") as f:
    test_cases = json.load(f)

for i, case in enumerate(test_cases, 1):
    result = Solution().minMax(case["input"]["arr"], case["input"]["m"])
    if result != case["output"]:
        print("Oh Noooo, Test Failed 🥲")
        print("Input: ", case["input"]["arr"])
        print("Got: ", result)
        print("Expected: ", case["output"])
        print()
    else:
        print("Oh yayyyy, Test Passed 😎")
        print("Input: ", case["input"]["arr"])
        print("Got: ", result)
        print("Expected: ", case["output"])
        print()


