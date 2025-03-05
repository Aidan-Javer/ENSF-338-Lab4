import timeit
from matplotlib import pyplot as plt
import numpy as np
import random
   
## Part 1 ##

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data_list):
        self.head = None
        for data in data_list:
            self.append(data)

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

## Part 2 ##

    def find_middle(self, start, last):
        if start is None:
            return None
        if start == last:
            return start

        slow = start
        fast = start.next

        while fast != last:
            fast = fast.next
            slow = slow.next
            if fast != last and fast is not None:
                fast = fast.next
        return slow

    def binary_search(self, num):
        start = self.head
        last = None

        while start != last:
            mid = self.find_middle(start, last)
            if mid is None:
                break
            if mid.data == num:
                return True
            elif mid.data > num:
                last = mid
            else:
                start = mid.next
        return -1

## Part 3 ## 
class Array:
    def __init__(self, data_list):
        if data_list is None:
            self.data = []
        else:
            self.data = data_list

        
    def binary_search(self, key):
        lo = 0
        hi = len(self.data) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.data[mid] == key:
                return mid
            elif self.data[mid] < key:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

## Part 4 ##
"""
The complexity of binary search on a linked list is O(n). The derivation is as follows: firstly, binary serach for a linked list
can be broken into two smaller instructions, find middle and divide to find target. The instruction to find middle each time the Array is broken up has complexity O(n/2) = O(n) because the the fast pointer used to find the end of the list moves through 2 nodes at a time making the step to find middle n/2. The instruction to divide the array has log(n) time complexity. Thus, the overall complexity would be O(n) for binary search on a linked list.
"""

## Part 5 ## 

def measure_time_linked_list(ll, target, iterations=100):
    t = timeit.timeit(lambda: ll.binary_search(target), number=iterations)
    return t / iterations

def measure_time_array(arr, target, iterations=100):
    """Measure the average execution time of the array binary search."""
    t = timeit.timeit(lambda: arr.binary_search(target), number=iterations)
    return t / iterations

avg_time_linked = []
avg_time_array = []

if __name__ == "__main__":
    listlengths = [1000, 2000, 4000, 8000]
    for listlength in listlengths:
        numbers = list(range(listlength))
        target = random.choice(numbers)

        ll = LinkedList(numbers)
        array = Array(numbers)
        
        time_ll = measure_time_linked_list(ll, target)
        time_array = measure_time_array(array, target)
        
        avg_time_linked.append(time_ll)
        avg_time_array.append(time_array)


    slope, intercept = np.polyfit(listlengths, avg_time_linked, 1)
    plt.scatter(listlengths, avg_time_array, label='Array Binary Search')
    linevalues = [slope * x + intercept for x in listlengths]
    plt.plot(listlengths, linevalues, 'r')

    log_lengths = np.log(listlengths) 
    slope, intercept = np.polyfit(log_lengths, avg_time_array, 1)
    plt.scatter(listlengths, avg_time_linked, label='Linked List Binary Search')
    linevalues = [slope * np.log(x) + intercept for x in listlengths]
    plt.plot(listlengths, linevalues, 'g')

    plt.xlabel('List Length')
    plt.ylabel('Average Time (seconds)')                                                    
    plt.legend()
    plt.show()
