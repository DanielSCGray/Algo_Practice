#  list-based class slStack​, with a singly linked list:

class StackNode:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None 

    def __str__(self) -> str:
        return f"<node {self.value}>"
    

class SLStack:
    def __init__(self) -> None:
        self.top = None

    def print_values(self):
        runner = self.top
        while runner != None:
            print(runner)
            runner = runner.next
        return self
# Stack Push
# Create push(val)​ that adds val to our stack.
    def push(self, val):
        new_node = StackNode(val)
        old_top = self.top
        new_node.next = old_top
        self.top = new_node
        return self
# Stack Top
# Return (not remove) the stack’s top value.
    def get_top(self):
        if self.top == None:
            print("Stack is empty")
            return self
        return self.top.value
    
# Stack Is Empty
# Return whether the stack is empty.
    def is_empty(self):
        return self.top == None 
# Stack Pop
# Create pop()​ to remove and return the top val.
    def pop_top(self):
        if self.is_empty():
            print("Stack is empty")
            return self
        old_top= self.top
        self.top = old_top.next
        return old_top.value

# Stack Contains
# Return whether given val is within the stack.
    def contains(self, val):
        if self.is_empty():
            print("Stack is empty")
            return self
        runner = self.top
        while runner != None:
            if runner.value == val:
                return True
            runner = runner.next
        return False
# Stack Size
# Return the number of stacked values.
    def size(self):
        stack_size = 0
        runner = self.top
        while runner != None:
            stack_size += 1
            runner = runner.next
        return stack_size


test =SLStack()
print(test.is_empty())
#true
test.push(1)
test.push(2)
test.push(3)
print(test.get_top())
#3
test.push(4)
print(test.get_top())
#4
print(test.is_empty())
#False
print(test.contains(4))
# True
test.pop_top()
print(test.contains(4))
# False
print(test.size())
#3

