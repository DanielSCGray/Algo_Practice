from single_linked_list2 import SingleLinkedList, SingleLinkedNode

# Sum List Numerals
# You are given two lists, each representing a number. Every node value is a 0-9 digit, with first node
# representing least significant digit. Return a new list representing the sum. Given 2=>0=>1 & 8=>4,
# return 0=>5=1 because 102 + 48 = 150.

def sum_l_n(list1, list2):
    sum = list_vals_converter(list1) + list_vals_converter(list2)
    new_list = SingleLinkedList()
    while sum > 0:
        val = sum % 10
        new_list.add_to_back(val)
        sum = sum // 10 

    return new_list


def list_vals_converter(sll):
    val_list = []
    runner = sll.head
    while runner != None:
        val_list.insert(0, str(runner.value))
        runner = runner.next
    num_str = "".join(val_list)
    num = int(num_str)
    return num





first_list = SingleLinkedList()
first_list.add_to_front(1)
first_list.add_to_front(0)
first_list.add_to_front(2)

second_list = SingleLinkedList()
second_list.add_to_front(4)
second_list.add_to_front(8)

first_list.print_values()
second_list.print_values()
# <node 2>
# <node 0>
# <node 1>
# <node 8>
# <node 4>
print(list_vals_converter(first_list))
#102 
test = sum_l_n(first_list, second_list)
test.print_values()
# <node 0>
# <node 5>
# <node 1>

# Second:​ what if first node is most​ significant?

def sum_l_n2(list1, list2):
    sum = list_vals_converter2(list1) + list_vals_converter2(list2)
    new_list = SingleLinkedList()
    while sum > 0:
        val = sum % 10
        new_list.add_to_front(val)
        sum = sum // 10 

    return new_list


def list_vals_converter2(sll):
    num_str = ""
    runner = sll.head
    while runner != None:
        num_str = num_str + str(runner.value)
        runner = runner.next
    num = int(num_str)
    return num


test2 = sum_l_n2(first_list, second_list)
test2.print_values()
# this time 201 + 84 = 285 should be in list as 2=>8=>5
# <node 2>
# <node 8>
# <node 5>