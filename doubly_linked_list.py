# Create DL list and node classes
# Include dList methods push(),pop(), front(), back(),
# contains(), and size().

class DoublyLinkedNode:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None
        self.prev = None
    
    def __str__(self) -> str:
        return f"<node {self.value}>"
    

class DoublyLinkedList:
    def __init__(self, head=None, tail=None) -> None:
        self.head = head
        self.tail = tail

    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner)
            runner = runner.next
        return self
    
    def append(self, val):
        node = DoublyLinkedNode(val)
        if self.tail == None:
            self.head = node
            self.tail = node
            return self
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        return self
    
    def pop(self):
        if self.head == self.tail:
            val = self.head.value
            self.head = None
            self.tail = None
            return val
        new_tail = self.tail.prev
        val = self.tail.value
        new_tail.next = None
        self.tail = new_tail
        return val
    
    def front(self):
        return None if self.head == None else self.head.value 
    
    def back(self):
        return None if self.tail == None else self.tail.value 
    
    def contains(self, val):
        runner = self.head
        while runner != None:
            if runner.value == val:
                return True
        return False
    
    def size(self):
        size = 0 
        runner = self.head
        while runner != None:
            size += 1
            runner = runner.next
        return size
    
# Prepend Value
# Given dList, new value, and existing value, insert new val into dList immediately before existing val.
    def prepend(self, new_val, existing_val):
        runner = self.head
        while runner.value != existing_val and runner != None:
            runner = runner.next
        if runner == None:
            print("value not found")
            return self
        node = DoublyLinkedNode(new_val)
        if runner == self.head:
            node.next = runner
            runner.prev = node
            self.head = node
        else:
            left_node = runner.prev
            left_node.next = node
            node.prev = left_node
            node.next = runner
            runner.prev = node
        return self
    

# Kth To Last Value
# Given k, return the value ‘k’ from a dList’s end.
    def kth_to_last(self, k):
        runner = self.tail
        while k > 1 and runner != None:
            runner = runner.prev
            k -= 1
        if runner == None:
            print("k is too large")
            return self
        return runner.value


# Palindrome
# Determine whether a dList is a palindrome
    def palindrome_check(self):
        left = self.head
        right = self.tail
        while left != None:
            if left.value != right.value:
                return False
            if left == right or left.next == right:
                break
            left = left.next
            right = right.prev
        return True

# Append Value
# Given dList, new value, and existing value, insert new val into dList immediately after existing val.
    def append_after(self, new_val, existing_val):
        runner = self.head
        while runner.value != existing_val and runner != None:
            runner = runner.next
        if runner == None:
            print("value not found")
            return self
        node = DoublyLinkedNode(new_val)
        if runner == self.tail:
            node.prev = runner
            runner.next = node
            self.tail = node
        else:
            right_node = runner.next
            right_node.prev = node
            node.prev = runner
            node.next = right_node
            runner.next = node
        return self
# Delete Middle Node
# Given a node in the middle of a dList, remove it.
    def del_middle_node(self, target_node: DoublyLinkedNode):
        if target_node == self.head or target_node == self.tail:
            return self
        left_node = target_node.prev
        right_node = target_node.next
        left_node.next = right_node
        right_node.prev = left_node
        return self
    
    def pop_middle_node(self, target_node: DoublyLinkedNode):
        if target_node == self.head or target_node == self.tail:
            return self
        left_node = target_node.prev
        right_node = target_node.next
        left_node.next = right_node
        right_node.prev = left_node
        return target_node
    

# Reverse
# Create function to reverse nodes in a dList.
    def reverse_list(self):
        if self.head == self.tail:
            return self
        old_tail = self.tail
        runner = self.tail.prev
        old_head = self.head
        while runner != old_head:
            left = runner.prev
            node = self.pop_middle_node(runner)
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
            runner = left
        old_head.prev = self.tail
        self.tail.next = old_head
        old_head.next = None
        self.tail = old_head
        old_tail.prev = None
        self.head = old_tail
        return self

    def get_min(self):
        if self.head == None:
            return self
        runner = self.head
        minimum = self.head.value
        while runner != None:
            if runner.value < minimum:
                minimum = runner.value
            runner = runner.next
        return minimum
    
    def get_max(self):
        if self.head == None:
            return self
        runner = self.head
        maximum = self.head.value
        while runner != None:
            if runner.value > maximum:
                maximum = runner.value
            runner = runner.next
        return maximum

# Partition
# Given dList and partition value, perform a simple partition (no need to return the pivot index).
# Break Loop
# Given dList that may contain a loop, break the loop while retaining original node order.












test = DoublyLinkedList()
test.append(1)
test.append(2)
test.print_values()

print(test.pop())
test.print_values()
    
print(test.front())
test.pop()
print(test.front())

test2 = DoublyLinkedList()
test2.append(1)
test2.append(2)
test2.append(3)
test2.append(5)
test2.prepend(4,5)
test2.print_values()
# <node 1>
# <node 2>
# <node 3>
# <node 4>
# <node 5>
print(test2.kth_to_last(2))
print(test2.kth_to_last(27))
# 4
# k is too large
pal = DoublyLinkedList()
pal.append(1)
pal.append(1)
pal.append(2)
pal.append(1)
pal.append(1)
print(pal.palindrome_check())
#True
pal.pop()
print(pal.palindrome_check())
# False

test2.print_values()
test2.reverse_list()
test2.print_values()
# <node 5>
# <node 4>
# <node 3>
# <node 2>
# <node 1>