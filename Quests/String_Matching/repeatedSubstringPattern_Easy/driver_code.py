import json
from repeatedSubstringPattern import Solution

sol = Solution()

with open("test_cases.json") as f:
    test_cases = json.load(f)

for i, test in enumerate(test_cases["tests"]):
    input = test["input"]
    expected = test["output"]
    output = sol.repeatedSubstringPattern(input)

    if output == expected:
        print("Bro Congrats 🫱🏿‍🫲🏽")
        print()
    else:
        print("What Bro, It's wrong bro")
        print("Naan Ketadhu: ", expected)
        print("Aana nee kuduthadhu: ", output)
        print("Enna, ", test["explanation"])
        print()
