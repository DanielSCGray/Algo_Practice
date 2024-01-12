# Flatten Child Lists
# Why limit nodes to contain only one pointer? For this challenge, each node has .next​ as always, but
# also a .child​ that is either null​ or points to the head of another list. Each node in those child lists
# might point to another list, and so on. Don’t alter .child​, but rearrange.next​ pointers to ‘flatten’ this
# hierarchy into a one linear list, from head node through all others via .next​.


class SingleLinkedNode:
    def __init__(self, val, child=None) -> None:
        self.value = val
        self.next = None
        self.child = child
    
    def __str__(self) -> str:
        return f"<node {self.value}> (child: {self.child})"
    

class SingleLinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner)
            runner = runner.next
        return self

    def print_values_and_decendents(self):
        runner = self.head
        while runner != None:
            print(runner)
            if runner.child != None:
                runner2 = runner.child
                while runner2 != None:
                    print(runner2)
                    if runner2.child != None:
                        runner3 = runner2.child
                        while runner3 != None:
                            print(runner3)
                            runner3 = runner3.next
                    runner2 = runner2.next

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
    
    def node_to_front(self, new_node):
        new_node.next = self.head
        self.head = new_node
        return self
    
    def node_to_back(self, new_node):
        if self.head == None:
            self.node_to_front(new_node)
            return self
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next =new_node
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
    
    def set_child_at_val(self, val, child_val):
        if self.head == None:
            return self
        runner = self.head
        while runner != None:
            if runner.value == val:
                runner.child = SingleLinkedNode(child_val)
                return self
            runner = runner.next
        print("val not found")
        return self
    
    def set_list_as_child_at_val(self, val, child_list):
        if self.head == None:
            return self
        runner = self.head
        while runner != None:
            if runner.value == val:
                runner.child = child_list.head
                return self
            runner = runner.next
        print("val not found")
        return self


parent_list = SingleLinkedList()

parent_list.add_to_back("Parent 1")
parent_list.add_to_back("Parent 2")
parent_list.add_to_back("Parent 3")
parent_list.add_to_back("Parent 4")
parent_list.add_to_back("Parent 5")

parent_list.print_values()

#Child nodes will be tracked by assigning their parents number then their number so parent 1's child is child 1.1, 1.2 etc parent 3's child is child 3.1 skipping designation child 2.1
#each child is head of their own list according to the prompt
child_list1 = SingleLinkedList()
child_list1.add_to_back("Child 1.1")
child_list1.add_to_back("Child 1.2")
child_list1.add_to_back("Child 1.3")
child_list1.add_to_back("Child 1.4")

child_list3 = SingleLinkedList()
child_list3.add_to_back("Child 3.1")
#grandkids use the same system, the below list will be the child of child 1.2
grandchild_list1_2 = SingleLinkedList()
grandchild_list1_2.add_to_back("Grandchild 1.2.1")
grandchild_list1_2.add_to_back("Grandchild 1.2.2")
grandchild_list1_2.add_to_back("Grandchild 1.2.3")
grandchild_list1_2.add_to_back("Grandchild 1.2.4")

parent_list.set_list_as_child_at_val("Parent 1", child_list1)
parent_list.set_list_as_child_at_val("Parent 3", child_list3)
child_list1.set_list_as_child_at_val("Child 1.2", grandchild_list1_2)

# parent_list.print_values()

# parent_list.print_values_and_decendents()

# <node Parent 1> (child: <node Child 1.1> (child: None))
# <node Child 1.1> (child: None)
# <node Child 1.2> (child: <node Grandchild 1.2.1> (child: None))
# <node Grandchild 1.2.1> (child: None)
# <node Grandchild 1.2.2> (child: None)
# <node Grandchild 1.2.3> (child: None)
# <node Grandchild 1.2.4> (child: None)
# <node Child 1.3> (child: None)
# <node Child 1.4> (child: None)
# <node Parent 2> (child: None)
# <node Parent 3> (child: <node Child 3.1> (child: None))
# <node Child 3.1> (child: None)
# <node Parent 4> (child: None)
# <node Parent 5> (child: None)


    #My flatten function should make it so print values will print all the info above but as a single linesr list in generational order
    #1 find last node in the list 
    #2 last.next = child
    #3 update last.next
    #4 continue scanning for child != None

def flatten_list(linked_list: SingleLinkedList) -> SingleLinkedList:
    runner = linked_list.head
    while runner.next != None:
        runner = runner.next
    last_node = runner
    runner = linked_list.head
    while runner != None:
        if runner.child != None:
            last_node.next = runner.child
            while last_node.next != None:
                last_node = last_node.next
        runner  = runner.next
    return linked_list

flatten_list(parent_list)

parent_list.print_values()

# <node Parent 1> (child: <node Child 1.1> (child: None))
# <node Parent 2> (child: None)
# <node Parent 3> (child: <node Child 3.1> (child: None))
# <node Parent 4> (child: None)
# <node Parent 5> (child: None)
# <node Child 1.1> (child: None)
# <node Child 1.2> (child: <node Grandchild 1.2.1> (child: None))
# <node Child 1.3> (child: None)
# <node Child 1.4> (child: None)
# <node Child 3.1> (child: None)
# <node Grandchild 1.2.1> (child: None)
# <node Grandchild 1.2.2> (child: None)
# <node Grandchild 1.2.3> (child: None)
# <node Grandchild 1.2.4> (child: None)