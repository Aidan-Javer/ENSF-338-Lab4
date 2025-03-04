import numpy as np
import matplotlib.pyplot as plt
import timeit

class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_head(self, node):
        node._next = self.head
        self.head = node
        self.size += 1
    
    def insert_tail(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current._next is not None:
                current = current._next
            current._next = node
        self.size += 1
    
    def get_size(self):
        return self.size
    
    def get_element_at_pos(self, pos):
        if pos < 0 or pos >= self.size:
            return None
        current = self.head
        for _ in range(pos):
            current = current._next
        return current

    def reverse_original(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode._value)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode._next = currNewNode
            prevNode = currNewNode
        self.head = newhead
    
    def reverse_updated(self):
        prev = None
        current = self.head
        while current is not None:
            next = current._next
            current._next = prev
            prev = current
            current = next
        self.head = prev

if __name__ == "__main__":
    listLengths = [1000, 2000, 3000, 4000]
    originalTimes = []
    updatedTimes = []
    for length in listLengths:
        elapsedTimes = []
        list = LinkedList()
        for i in range(length):
            list.insert_head(Node(i))
        elapsedTimes = timeit.repeat(lambda: list.reverse_original(), number=20, repeat=5)
        originalTimes.append(min(elapsedTimes))

        elapsedTimes = []
        list = LinkedList()
        for i in range(length):
            list.insert_head(Node(i))
        elapsedTimes = timeit.repeat(lambda: list.reverse_updated(), number=20, repeat=5)
        updatedTimes.append(min(elapsedTimes))
    
    # NOTE: For I opted to instead perform the timing via timeit.repeat() 
    # instead of timeit.timeit(). Performing 100 runs with timeit.timeit() provided
    # inconsistent results. timeit.repeat() was more consistent. 100 runs are still performed,
    # over 5 repeats. The minimum time is taken from the 5 repeats.

    # Create a single plot
    fig, ax = plt.subplots(figsize=(10, 5))

    # Line plot: Original vs Updated
    ax.plot(listLengths, originalTimes, label="Original", color='blue')
    ax.plot(listLengths, updatedTimes, label="Updated", color='orange')
    
    ax.set_xlabel("List Length")
    ax.set_ylabel("Time")
    ax.legend()
    ax.set_title("Original vs Updated Times")

    plt.tight_layout()
    plt.show()
    
