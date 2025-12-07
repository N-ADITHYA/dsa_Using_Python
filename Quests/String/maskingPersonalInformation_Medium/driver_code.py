import json
from maskPII import Solution

sol = Solution()

with open("test_cases.json") as f:
    test_cases = json.load(f)


for i, test in enumerate(test_cases):
    output = sol.maskPII(test["input"])
    input = test["input"]
    expected = test["output"]
    if output == expected:
        print("Passed Bro, Congrats!")
        print()
    else:
        print("Ohh, Sorry Fix your code man")
        print(f"Take this input {input} and \n Output is {output} \n Expected {expected}")
        print()