# rListLength
# Given the first node of a singly linked list, create
# a recursive function that returns the number of
# nodes in that list. You can assume the list
# contains no loops, and that it is short enough that
# you will not ‘blow your stack’.

from single_linked_list import SingleLinkedList, SingleLinkedNode


def rec_list_len(node: SingleLinkedNode):
    if node == None:
        return 0 
    sum = 1
    sum += rec_list_len(node.next)
    return sum


test = SingleLinkedList()
for i in range(1,6):
    test.add_to_back(i)
test.print_values()
# <node 1>
# <node 2>
# <node 3>
# <node 4>
# <node 5>
head_node = test.head

print(rec_list_len(head_node))
#5

