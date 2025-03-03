import sys
from matplotlib import pyplot as plt
import timeit

# Part 1: Growth Strategy Explanation (Question 1)
"""
Python's list growth strategy uses an over-allocation formula from lists.c:
new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3; The Growth Factor is 
approximately 12.5%.
"""

s = 0

# Part 2 ##

def track_capacity_changes(max_elements):
    lst = []
    prev_size = sys.getsizeof(lst)
    last_trigger_size = 0
    for i in range(max_elements):
        lst.append(i)
        current_size = sys.getsizeof(lst)
        if current_size != prev_size:
            print(f"Capacity changed at len={len(lst)} (new sizeof={current_size})")
            last_trigger_size = len(lst)
            prev_size = current_size
    return last_trigger_size - 1  

## Part 3 & 4 ##
def test_resize(lst):
    lst.append(1)
    lst.append(1)

def test_no_resize(lst):
    lst.append(1)     

## Part 2 ##

if __name__ == "__main__":
    s = track_capacity_changes(64) 
    print(f"Final S where resize occurs: {s}")

## Parts 3 & 4 ##
    lst = []
    for i in range (s - 1):
        lst.append(i)
    resize_times = timeit.repeat(lambda: test_resize(lst.copy()), repeat=1000, number=1)
    no_resize_times = timeit.repeat(lambda: test_no_resize(lst.copy()), repeat=1000, number=1)

    print(f"Avg resize time (S->S+1): {sum(resize_times)/len(resize_times):.8f} sec")
    print(f"Avg no-resize time (S-1->S): {sum(no_resize_times)/len(no_resize_times):.8f} sec")

## Part 5 ##

    plt.hist(resize_times, bins=30, alpha=0.5, label='Resize (S -> S+1)')
    plt.hist(no_resize_times, bins=30, alpha=0.5, label='No Resize (S-1 -> S)')
    plt.xlabel("Time (seconds)")
    plt.ylabel("Frequency")
    plt.title("Append Operation Time Distribution")
    plt.legend()
    plt.show()


"""
Going from a list size of S -> S + 1 should take longer than S - 1 -> S because the first operation involves the deallocation and reallocation
of new memory, whereas the second operation requires adding/appending the new element without having to resize the list. However,
the pyton compiler is extremely quick at reallocating memory that the time is nearly untraceable.
"""
