from Quests.Linked_List import linkedListBuilder
import removeDuplicates
import json


with open("test_cases.json") as f:
    test_cases = json.load(f)

for i, test in enumerate(test_cases):
    link = linkedListBuilder.LinkedList() # this line is responsible for building a simple linkedlist from the given List😎
    head = test["input"]
    for n in head:
        link.add_node(n) # this line will actually build the linkedlist
    ll = link.ret() # self.head will be returned

    obj = removeDuplicates.Solution()
    data = obj.deleteDuplicates(ll) # main logic


    def print_output(head_node):
        cur = head_node
        out = []
        while cur:
            out.append(cur.val)
            cur = cur.next
        return out

    if print_output(data) == test["expectedOutput"]:
        print("Passed")
        print("Output: ", print_output(data))
        print("Expected", test["expectedOutput"])
        print()
    else:
        print("Wrong")
        print("Output: ", print_output(data))
        print("Expected", test["expectedOutput"])
        print()



