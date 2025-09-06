import json
from trap_Normal_Soln import Solution
from trap_Optimized_Soln import Solution as d


with open("test_cases.json") as f:
    test_cases = json.load(f)


for i, case in enumerate(test_cases, 1):
    result = Solution().trap(case["input"]["height"])
    resultO = d().trapO(case["input"]["height"])


    if result != case["output"]:
        print("Normal Soln")
        print("Oh noooo, It's failed 😔")
        print("Input: ", case["input"]["height"])
        print("Expected: ", case["output"])
        print("Got: ", result)
        print()
    else:
        print("Normal Soln")
        print("Oh Yeahhhh, It's passed 😎")
        print("Input: ", case["input"]["height"])
        print("Expected: ", case["output"])
        print("Got: ", result)
        print()

for i, case in enumerate(test_cases, 1):
    resultO = d().trapO(case["input"]["height"])
    if resultO != case["output"]:
        print("For optimized Soln")
        print("Oh noooo, It's failed 😔")
        print("Input: ", case["input"]["height"])
        print("Expected: ", case["output"])
        print("Got: ", resultO)
        print()
    else:
        print("For optimized Soln")
        print("Oh Yeahhhh, It's passed 😎")
        print("Input: ", case["input"]["height"])
        print("Expected: ", case["output"])
        print("Got: ", resultO)
        print()