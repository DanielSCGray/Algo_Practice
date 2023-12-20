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













# first_node = SingleLinkedNode(0)



# test = SingleLinkedList(first_node)
test = SingleLinkedList()

test.add_to_front(3)

test.add_to_front(2)
test.add_to_front(1)
test.add_to_back(4)

test.print_values()
# test.remove_head()
# test.print_values()
print(test.contains(4))
print(test.contains(14))
print(test.length())
# print(test.average())
# test.remove_from_back()
test.remove_value(12)
test.prepend_value(22,5)
test.prepend_value(22,4)
test.append_value(23, 22)
test.print_values()
print("***")
# second_list = test.split_on_value(3)
# second_list.print_values()
# print("*****")
# test.print_values()
test.partition_on_value(22)
test.print_values()

duptest = SingleLinkedList()
duptest.add_to_front(3)
duptest.add_to_front(3)
duptest.add_to_front(3)
duptest.add_to_front(2)
duptest.add_to_front(1)
duptest.print_values()
# duptest.de_duplicate()
duptest.de_dupe_without_buffer()
print("***")
duptest.print_values()