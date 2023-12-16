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
test.print_values()