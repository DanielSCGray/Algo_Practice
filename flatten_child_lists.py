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

    def add_to_front(self, val, child=None):
        new_node = SingleLinkedNode(val)
        new_node.next = self.head
        self.head = new_node
        return self
    

    def add_to_back(self, val, child=None):
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
    
