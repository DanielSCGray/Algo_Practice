#this is practice building the queue data structure to better understand it. I am aware of python's collection library

class QueueNode:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None

    def __str__(self) -> str:
        return f"<node {self.value}>"
    

class PracticeQueue:
    def __init__(self) -> None:
        self.front = None
        self.back = None

    def print_values(self):
        runner = self.front
        while runner != None:
            print(runner)
            runner = runner.next
        return self
    
    def enqueue(self, val):
        new_node = QueueNode(val)
        if self.front == None:
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node
        return self
    
    def dequeue(self):
        if self.front == None:
            print("Queue is empty")
            return self
        new_front = self.front.next
        value = self.front.value
        self.front = new_front
        return value

    def get_front(self):
        if self.front == None:
            print("Queue is empty")
            return self
        return self.front.value
    
    def contains(self, val):
        runner = self.front
        while runner != None:
            if runner.value == val:
                return True
        return False
    
    def is_empty(self):
        if self.front == None:
            return True
        return False
    
    def size(self):
        queue_size = 0
        if self.front == None:
            return queue_size
        runner = self.front
        while runner != None:
            queue_size += 1
            runner = runner.next
        return queue_size








test = PracticeQueue()
test.enqueue(1)
test.enqueue(2)
test.enqueue(3)
test.print_values()
# <node 1>
# <node 2>
# <node 3>

print(test.dequeue())
test.print_values()
# 1
# <node 2>
# <node 3>
print(test.get_front())
test.print_values()
# 2
# <node 2>
# <node 3>
print(test.size())
# 2
test.enqueue(4)
print(test.size())
# 3


