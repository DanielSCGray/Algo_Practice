from single_linked_list2 import SingleLinkedList, SingleLinkedNode

# Setup List Loop
# In preparation for tomorrow, create a sequence of slNode​s that form a closed loop. Your function’s first
# argument should signify how many nodes total, and the second should be which node number is
# pointed to by the last node. Give nodes sequential numbers as values, for clarity. Callling setupLoop(5,
# 3) should return a circular list of 1=>2=>3=>4=>5=>3=>4=>5=>3....

def build_loop_list(list_length: int, loop_location: int): 
    my_list = SingleLinkedList()
    my_list.head = SingleLinkedNode(1)
    runner = my_list.head
    loop_node = None
    for i in range(2, list_length + 1):
        runner.next = SingleLinkedNode(i)
        if runner.value == loop_location:
            loop_node = runner
        runner = runner.next
    runner.next = loop_node
    return my_list

def safe_print(my_list:SingleLinkedList):
    runner = my_list.head
    vals = []
    dupe_count = 0
    while runner != None:
        print(runner)
        if runner.value in vals:
            dupe_count += 1
        vals.append(runner.value)
        if dupe_count > 3:
            break
        runner = runner.next
    return my_list

test = build_loop_list(5,3)
safe_print(test)
# <node 1>
# <node 2>
# <node 3>
# <node 4>
# <node 5>
# <node 3>
# <node 4>
# <node 5>
# <node 3>

# Has Loop
# Given a linked list, determine whether it has a
# loop, and return a boolean accordingly.
def loop_check(my_list: SingleLinkedList) -> bool:
    runner = my_list.head
    while runner.next != None:
        if runner.value > runner.next.value:
            return True
        runner = runner.next
    return False
    #I fixed the bad runtime inherent in the safeprint function design by using the logic of the loop constructor -> .next is only smaller if we're looping
print(loop_check(test))
#True

# Break Loop
# Given a linked list, determine whether there is a
# loop, and if so, break it. Retain all nodes, in
# original order.
def loop_break(my_list: SingleLinkedList) -> SingleLinkedList:
    runner = my_list.head
    while runner.next != None:
        if runner.value > runner.next.value:
            runner.next = None
            break
        runner = runner.next
    return my_list

loop_break(test)
test.print_values()
# <node 1>
# <node 2>
# <node 3>
# <node 4>
# <node 5>

# Loop Start
# Given a linked list, return a pointer to the node
# where loop begins (where last node points), or
# null if no loop.
def loop_start(my_list: SingleLinkedList) -> SingleLinkedNode:
    runner = my_list.head
    bad_node = None
    while runner.next != None:
        if runner.value > runner.next.value:
            bad_node = runner.next
            break
        runner = runner.next
    return bad_node

test2 = build_loop_list(7,4)
print(loop_start(test2))
#<node 4>


# Number of Nodes
# Given a linked list with or without a loop, return
# total number of nodes. Given circular list
# (a)=>(b)=>(c)=>(d)=>(e)=>(c), return 5.
def node_count(my_list: SingleLinkedList) -> int:
    runner = my_list.head
    count = 1
    while runner.next != None:
        if runner.value > runner.next.value:
            break
        runner = runner.next
        count += 1
    return count

print(node_count(test))
#5
print(node_count(test2))
#7
#works on both looping and non looping lists