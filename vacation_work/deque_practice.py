class DQNode:
    def __init__(self, val) -> None:
        self.value = val
        self.prev = None
        self.next = None

    def __str__(self) -> str:
        return f"node {self.value}"


class DequePractice:
    def __init__(self) -> None:
        self.front = None
        self.back = None
        self.size = 0


    def print_values(self):
        if self.front == None:
            print("Dequeue is empty")
        else:
            runner = self.front
            while runner != None:
                print(runner)
                runner = runner.next
        return self

# pushFront(val)​,
    def push_front(self, val):
        new_node = DQNode(val)
        if self.front == None:
            self.front = new_node
            self.back = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1
        return self
        

#  pushBack(val)​,
    def push_back(self, val):
        new_node = DQNode(val)
        if self.back == None:
            self.back = new_node
            self.front = new_node
        else:
            new_node.prev = self.back
            self.back.next = new_node
            self.back = new_node
        self.size += 1
        return self
    


#  popFront()​,
    def pop_front(self):
        if self.front == None:
            return self
        popped = self.front
        new_front = popped.next
        if new_front != None:
            new_front.prev = None
        self.front = new_front
        self.size -= 1
        return popped.value
    
#  popBack()​,
    def pop_back(self):
        if self.back == None:
            return self
        popped = self.back
        new_back = popped.prev
        if new_back != None:
            new_back.next = None
        self.back = new_back
        self.size -= 1
        return popped.value
    

        
# front()​,
    def get_front(self):
        if self.size == 0:
            print("Empty list")
        return self if self.size == 0 else self.front.value
#  back()​, 
    def get_back(self):
        if self.size == 0:
            print("Empty list")
        return self if self.size == 0 else self.back.value
# contains(val)​, 
    def contains_val(self, search_val):
        runner = self.front
        while runner != None:
            if runner.value == search_val:
                return True
            runner = runner.next
        return False

# isEmpty()
    def is_empty(self):
        return self.size == 0
# size()​.
    def get_size(self):
        print(self.size)
        return self.size



test = DequePractice()
test.push_front(1)
test.print_values()
print("**")
test.push_back(2)
test.push_back(3)
test.print_values()
test.get_size()
print(test.get_front())
print(test.get_back())
print(test.contains_val(1))
print(test.contains_val(4))
print(test.is_empty())
