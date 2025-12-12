from Quests.Linked_List import linkedListBuilder
from reverseList import Solution
import json

with open("test_cases.json") as f:
    test_cases = json.load(f)

for test in test_cases["tests"]:
    inp = test["input"]
    link = linkedListBuilder.LinkedList()
    sol = Solution()
    for i in inp:
        if i:
            link.add_node(i)
    ret = link.ret()
    output = sol.reverseList(ret)


    def print_output(head_node):
        cur = head_node
        out = []
        while cur:
            out.append(cur.val)
            cur = cur.next
        return out

    if print_output(output) == test["output"]:
        print("Ho gaya🫱🏿‍🫲🏽 beta sabaash")
        print()