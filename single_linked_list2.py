#Will create SLL and SLNode classes and build out various features 

class SingleLinkedNode:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None
    
    def __str__(self) -> str:
        return f"<node {self.value}>"
    

class SingleLinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner)
            runner = runner.next
        return self

    def add_to_front(self, val):
        new_node = SingleLinkedNode(val)
        new_node.next = self.head
        self.head = new_node
        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = SingleLinkedNode(val)
        return self 
    
    def remove_head(self):
        if self.head == None:
            return None
        old_head = self.head
        new_head = old_head.next
        old_head.next = None
        self.head = new_head
        return self
    
    def remove_from_back(self):
        if self.head == None:
            return None
        runner = self.head
        if runner.next == None:
            self.remove_head()
            return self
        new_back = self.head
        while runner.next != None:
            new_back = runner
            runner = runner.next
        new_back.next = None
        return self
    
    
    def contains(self, val):
        runner = self.head
        while runner != None:
            if runner.value == val:
                return True
            runner = runner.next
        return False
    
    #return list length
    def length(self):
        if self.head == None:
            return 0
        list_len = 0
        runner = self.head
        while runner != None:
            list_len += 1
            runner = runner.next
        return list_len
    
    #return average of all node values
    def average(self):
        if self.head == None:
            return 0
        total_nodes = self.length()
        total_vals = 0 
        runner = self.head
        while runner != None:
            total_vals += runner.value
            runner = runner.next
        return total_vals / total_nodes
    
    def remove_value(self, val):
        runner = self.head 
        #edge case if value is the front
        if runner.value == val:
            self.remove_head()
            return self
        #initialize target node var outside the loop to track if the val is found
        target_node = None
        prev_node = runner
        while runner != None:
            if runner.value == val:
                target_node = runner
                break
            prev_node = runner
            runner = runner.next
        #target node is still none? => the val wasn't in the list
        if target_node == None:
            print(f"{val} not found in list.")
            return self
        if target_node.next == None:
            prev_node.next = None
            return self
        prev_node.next = target_node.next
        # target_node.next = None
        return self
    
    #place a node ahead of a node with the specified value in arg "before"
    def prepend_value(self, val, before):
        if self.head == None:
            print("list is empty")
            return self
        runner = self.head
        if runner.value == before:
            self.add_to_front(val)
            return self
        target_node = None
        prev_node = runner
        while runner != None:
            if runner.value == before:
                target_node = runner
                break
            prev_node = runner
            runner = runner.next
        if target_node == None:
            print(f"{before} not found in list. No action taken")
            return self
        new_node = SingleLinkedNode(val)
        prev_node.next = new_node
        new_node.next = target_node
        return self
    
    def append_value(self, val, after):
        if self.head == None:
            print("list is empty")
            return self
        runner = self.head
        target_node = None
        while runner != None:
            if runner.value == after:
                target_node = runner
                break
            runner = runner.next
        if target_node == None:
            print(f"{after} is not in the list. No action taken")
            return self
        new_node = SingleLinkedNode(val)
        old_link = target_node.next
        target_node.next = new_node
        new_node.next = old_link
        return self
    
    #split on value: Create a function​ that, given
# number​, splits a list in two. The latter half of the
# list should be returned, starting with node
# containing num​. E.g.: splitOnVal(5)​ for the list
# (1 >3>5>2>4) will change list to (1>3) and return
# value will be (5>2>4).
    
    def split_on_value(self, target_val):
        if self.head == None:
            print("list is empty")
            return self
        runner = self.head
        if runner.value == target_val:
            print("cannot split list at head")
            return self
        target_node = None
        prev_node = runner
        while runner != None:
            if runner.value == target_val:
                target_node = runner
                break
            prev_node = runner
            runner = runner.next
        if target_node == None:
            print(f"split value {target_val} not found. No action taken.")
            return self
        new_list = SingleLinkedList(target_node)
        prev_node.next = None
        return new_list
    
# partition
# Create partition(list,value)​ that locates the
# first node with that value, and moves all nodes
# with values less than that value to be earlier, and
# all nodes with values greater than that value to
# be later. Otherwise, original order need not be
# perfectly preserved.
    
    #based on the prompt I will assume the partition value is unique. my solution will delete and remake identical nodes.
    def partition_on_value(self, partition_val):
        if self.head == None:
            print("list is empty")
            return self
        runner = self.head
        if runner.next == None:
            print("cannot partition a list with only one node")
            return self
        if self.contains(partition_val) == False:
            print(f"partition value {partition_val} is not in the list.")
            return self
        if runner.value != partition_val:
            self.remove_value(partition_val)
            self.add_to_front(partition_val)
            runner = self.head
        prev_node = runner
        while runner != None:
            if runner.value >= partition_val:
                prev_node = runner
            else:
                next_node = runner.next
                prev_node.next = next_node
                self.add_to_front(runner.value)
            runner = runner.next
        return self
# dedupeList
# Remove nodes with duplicate values. Following
# this call, all nodes remaining in the list should
# have unique values. Retain only the first instance
# of each value.
    
    #plan is to use a hashmap to track values and remove/retain nodes accordingly
    def de_duplicate(self):
        hashmap = {}
        runner = self.head
        prev_node = runner
        while runner != None:
            if runner.value in hashmap:
                prev_node.next = runner.next
            else:
                hashmap[runner.value] = runner.value
                prev_node = runner
            runner = runner.next
        return self
    
# dedupeListWithoutBuffer
# Can you accomplish this without using a
# secondary buffer? What are the performance
# ramifications?

    #this can be done easily via brute force but has the negative performance ramification of an O(n^2) runtime

    def de_dupe_without_buffer(self):
        first_runner = self.head
        if first_runner == None or first_runner.next == None:
            return self
        while first_runner != None:
            prev_node = first_runner
            second_runner = first_runner.next
            while second_runner != None:
                if second_runner.value == first_runner.value:
                    prev_node.next = second_runner.next
                else:
                    prev_node = second_runner
                second_runner = second_runner.next
            first_runner = first_runner.next
        return self

# Reverse
# Reverse the sequence of nodes in the list.

    def reverse(self):
        if self.head == None:
            print("list is empty")
            return self
        runner = self.head
        if runner.next == None:
            return self
        runner = runner.next
        val_list = []
        while runner != None:
            val_list.append(runner.value)
            runner = runner.next
        self.head.next = None
        for i in range(len(val_list)):
            v = val_list.pop(0)
            self.add_to_front(v)
        return self

# KthLast
# Given k, return the value that is ‘k’ nodes from
# the list’s end. If given (list,1)​, return the list’s
# last value. If given (list,4)​, return the value at
# the node that has exactly 3 nodes following it.

    def kth_last(self, k):
        length = self.length()
        if k > length:
            print(f"k must be less than or equal to list length ({length})")
            return self
        runner = self.head
        while k != length:
            runner = runner.next
            length -= 1
        return runner.value
    

# Is Palindrome
# Return whether a list is a palindrome. String
# palindromes read the same front-to-back and
# back-to-front. Here, compare node values. N.B.:
# to be accurate in JavaScript, use ===​ instead of
# ==​, since 1 == true == [1] == "1"​.


    def is_palindrome(self):
        if self.head == None:
            return True
        runner = self.head
        if runner.next == None:
            return True
        val_list = []
        while runner != None:
            val_list.append(runner.value)
            runner = runner.next
        i = 0 
        j = len(val_list) - 1
        while j > i:
            if val_list[i] != val_list[j]:
                return False
            i += 1
            j -= 1
        return True
    
# Second:​ depending on environment, you might
# not have plentiful memory available. Can you
# solve this without using an additional array?
    def is_palindrome2(self):
        if self.head == None:
            return True
        runner = self.head
        if runner.next == None:
            return True
        length = self.length()
        left = 1
        right = length
        while right > left:
            runner = self.head
            counter = 1
            while runner != None:
                if counter == left:
                    left_val = runner.value
                elif counter == right:
                    right_val = runner.value
                    if right_val == left_val:
                        break
                    else:
                        return False
                counter += 1
                runner = runner.next
            left += 1
            right -= 1
        return True

# Shift List
# Given a list, shift nodes to the right, by a given number shiftBy. These shifts are circular: i.e. when
# shifting a node off list’s end, it should reappear at list’s start. For list (a)=>(b)=>(c), shift(1) should return
# (c)=>(a)=>(b).


    def shift_by(self, shift):
        length = self.length()
        #control for circular shifts
        shift = shift % length
        counter = 1
        new_last = None
        shift_point = length - shift
        old_head = self.head
        runner = self.head
        while length >= counter:
            if counter == shift_point:
                new_last = runner
            if counter == shift_point + 1:
                self.head = runner
            if counter == length:
                runner.next = old_head
            runner = runner.next
            counter += 1
        new_last.next = None
        return self

# Second:​ also handle negative shiftBy (to left).
    def shift_by_left(self, shift):
        length = self.length()
        #control for circular shifts
        shift = shift % length
        if shift == 0:
            return self
        counter = 1
        new_last = None
        old_head = self.head
        runner = self.head
        while length >= counter:
            if shift == counter:
                new_last = runner
            if shift + 1 == counter:
                self.head = runner
            if counter == length:
                runner.next = old_head
            runner = runner.next
            counter += 1
        new_last.next = None
        return self



# test = SingleLinkedList(first_node)
test = SingleLinkedList()

test.add_to_front(3)

test.add_to_front(2)
test.add_to_front(1)
test.add_to_back(4)

test.print_values()
# <node 1>
# <node 2>
# <node 3>
# <node 4>
# test.reverse()
# test.print_values()
# <node 4>
# <node 3>
# <node 2>
# <node 1>
print(test.kth_last(2))
#2 (2 is 2nd to last since list was reversed)
print(test.is_palindrome())
#False
pal_test = SingleLinkedList()
pal_test.add_to_front(2)
pal_test.add_to_front(1)
pal_test.add_to_front(2)
print(pal_test.is_palindrome())
#True
print(test.is_palindrome2())
#False
print(pal_test.is_palindrome2())
#True

test.print_values()
# <node 1>
# <node 2>
# <node 3>
# <node 4>
test.shift_by(2)
test.print_values()

# <node 3>
# <node 4>
# <node 1>
# <node 2>
#success!
test.shift_by_left(3)
test.print_values()
# <node 2>
# <node 3>
# <node 4>
# <node 1>
#success!
print("***************************")
