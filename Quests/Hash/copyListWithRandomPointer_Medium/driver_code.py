from json import load
from specialLinkedlistBuilder import SpecialLinkedList
from copyRandomList import Solution

with open("test_cases.json") as f:
    test_cases = load(f)


def serialize_list(head):
    nodes = []
    index_map = {}

    curr = head
    idx = 0
    while curr:
        nodes.append(curr)
        index_map[curr] = idx
        curr = curr.next
        idx += 1

    result = []
    for node in nodes:
        rand_idx = index_map[node.random] if node.random else None
        result.append([node.val, rand_idx])

    return result




for test in test_cases["tests"]:
    sp = SpecialLinkedList()
    solver = Solution()

    original = sp.array_to_special_linkedlist(test["input"])
    copied = solver.copyRandomList(original)

    actual = serialize_list(copied)

    print("Test:", test["name"])
    print("Expected:", test["output"])
    print("Actual  :", actual)

    if actual == test["output"]:
        print("PASS\n")
    else:
        print("FAIL\n")




