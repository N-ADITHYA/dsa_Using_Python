from Quests.Linked_List import linkedListBuilder
from oddEvenList import Solution
import json



with open("test_cases.json") as f:
    test_cases = json.load(f)

for test in test_cases["tests"]:
    sol = Solution()
    link = linkedListBuilder.LinkedList()
    for i in test["input"]:
        if i:
            link.add_node(i)
    data = link.ret()
    head_node = sol.oddEvenList(data)


    def print_output(head_node):
        cur = head_node
        out = []
        while cur:
            out.append(cur.val)
            cur = cur.next
        return out


    if print_output(data) == test["expected"]:
        print("Passed")
        print("Output: ", print_output(data))
        print("Expected", test["expected"])
        print()
    else:
        print("Wrong")
        print("Output: ", print_output(data))
        print("Expected", test["expected"])
        print()
