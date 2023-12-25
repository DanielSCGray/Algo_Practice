#Because of the one-way direction of singly linked lists, using a list to implement a Queue feels natural.
#What if we wanted to use an underlying Array?
# When Queue’s tail or head approaches ‘size’, wrap around to [0] and continue. We cannot let tail and
# head meet – one can’t “lap” the other. Instead, enqueue(val) should fail: Queue is full. Ditto dequeue() if
# Queue is empty. Constructor requires a size argument. 

    #cap represeents the upper bound on array size
    #there will be no held/empty array spaces?
    #the prompt seems unclear... python lists can pop by index, so if I list.pop(0) the list will pop the front and update indexes so the new front is at idx 0
    #this kind of renders the premise obsolete...
    #I think the point is to show I can use pointers to circle around past zero
    #For the sake of the question I will treat the list as a C# style Array with an immutable size
class CircularQueue:
    def __init__(self, cap) -> None:
        self.front_idx = 0
        self.back_idx = 0
        self.size = 0
        self.cap = cap
        self.underlying_array = [None] * cap


    def print_info(self):
        print(f"front id = {self.front_idx}, front value = {self.underlying_array[self.front_idx]}")
        print(f"back id = {self.back_idx}, back value = {self.underlying_array[self.back_idx]}")
        print(self.underlying_array)
        return self

# Enqueue
# Create enqueue(val) that adds val to our circular queue. Return false on fail. Wrap if needed!
    def enqueue(self, val):
        #check if adding to the list causes front and back indexes to overlap => if so we're full
        if self.back_idx +1 == self.front_idx or (self.back_idx + 1 == self.cap and self.front_idx == 0):
            print("Failure, list is full")
            return self
        #check for an empty list, if so we "soft reset" everything back to the start of the list (idx 0)
        if self.size == 0:
            self.underlying_array[0] = val
            self.front_idx = 0
            self.back_idx = 0
        elif self.back_idx + 1 < self.cap:
            self.back_idx +=1
            self.underlying_array[self.back_idx] = val
        elif self.back_idx + 1 == self.cap:
            #else would suffice here but I am being explicit and writing out the condition for clarity 
            self.back_idx = 0
            self.underlying_array[self.back_idx] = val
        #add to size to count the newly added value
        self.size += 1 
        return self
        
# Front
# Return (not remove) the queue’s front value.
    def get_front(self):
        return self.underlying_array[self.front_idx]
# Is Empty
# Return whether queue is empty.
    def is_empty(self):
        return self.size == 0
# Is Full
# Return whether queue is full.
    def is_full(self):
        return self.size == self.cap



# Dequeue
# Create cirQueue method dequeue() that removes and returns the front value. Return null on fail.
    def dequeue(self):
        if self.size == 0:
            print("failure, list is empty")
            return self
        front_val = self.underlying_array[self.front_idx]
        self.size -= 1
        self.underlying_array[self.front_idx] = None
        if self.front_idx + 1 == self.cap:
            self.front_idx = 0 
        else:
            self.front_idx += 1
        return front_val
        





# Contains
# Return whether given val is within the queue.
    def contains(self, search_val):
        return search_val in self.underlying_array
# Size
# Return number of queued vals (not capacity).
    def get_size(self):
        return self.size
# Grow
# (advanced) Create method grow(newSize) that expands the circular queue to a new given size.
    # note: I am choosing to opperate on the existing list rather than the easier prospect of creating a new list and saving it over the previous
    def grow_list(self, new_cap):
        if new_cap <= self.cap:
            print(f"new size must be larger than current size of {self.cap}")
            return self
        #cap_diff will tell us how many None filled indicies nees to be added
        cap_dif = new_cap - self.cap
        if self.front_idx <= self.back_idx:
            added_nones = [None] * cap_dif
            self.underlying_array.extend(added_nones)
        else:
            if cap_dif >= self.back_idx + 1:
                for i in range(self.back_idx+1):
                    self.underlying_array.append(self.underlying_array[i])
                    self.underlying_array[i] = None
                remainder = cap_dif - self.back_idx -1
                self.back_idx = len(self.underlying_array) - 1
                if remainder > 0:
                    added_nones = [None] * remainder
                    self.underlying_array.extend(added_nones)
                
                
            else:
                j = cap_dif
                for i in range(self.back_idx +1):
                    if i < cap_dif:
                        self.underlying_array.append(self.underlying_array[i])
                    if j <= self.back_idx:
                        self.underlying_array[i] = self.underlying_array[j]
                    else:
                        self.underlying_array[i] = None
                    j += 1
                self.back_idx -= cap_dif
        self.cap = new_cap
        return self
        


test = CircularQueue(10)

test.print_info()

for i in range(10):
    test.enqueue(i)

test.print_info()

test.enqueue(10)

test.dequeue()
test.print_info()
test.enqueue(10)
test.print_info()
print(test.contains(1))
print(test.contains(12))
test.dequeue()
test.dequeue()
test.dequeue()
test.dequeue()
test.enqueue(11)
test.enqueue(12)
test.enqueue(13)
test.print_info()
test.grow_list(12)
test.print_info()