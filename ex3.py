import sys
from matplotlib import pyplot as plt
import timeit

## Part 1 ##
"""
Rresizing in the C programs works by allocating new memory when the max capacity has been reached: 
"new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;". Note that it oversizes the 
new memory location to add a buffer. Then, once new memory has been allocated it copies the items 
"self->ob_item = items;" in the old list into the newly allocated one.
"""
## Part 2,3,4 ##

s = 0

def test_resize():
    list = list(range(s))
    list = list[:]
    list.append(1)  
    return list


def test_no_resize():
    list = list(range(s - 1))
    list = list[:]  
    list.append(1)  
    return list

list = []
if __name__ in "__main__":
    prev_size = sys.getsizeof(list)
    for i in range(64):
        list.append(i)
        current_size = sys.getsizeof(list)
        if current_size != prev_size:
            print(f"After appending {i+1} element(s): size in bytes changed from {prev_size} to {current_size}")
            prev_size = current_size
    s = i + 1

    resize_times = timeit.repeat(lambda: test_resize(), repeat=1000, number=1)
    no_resize_times = timeit.repeat(lambda: test_no_resize(), repeat=1000, number=1)

    print("Average time for append with resize (S -> S+1):", sum(resize_times) / len(resize_times))
    print("Average time for append without resize (S-1 -> S):", sum(no_resize_times) / len(no_resize_times))

## Part 5 ## 

plt.hist(resize_times, bins=30, alpha=0.5, label='Resize (S -> S+1)')
plt.hist(no_resize_times, bins=30, alpha=0.5, label='No Resize (S-1 -> S)')
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency")
plt.title("Append Operation Time Distribution")
plt.legend()
plt.show()

"""
Going from a list size of S -> S + 1 takes significantly longer than S - 1 -> S because in the first operation involves the deallocation and reallocation
new memory, whereas the second operation requires adding/appending the new element without have to resize the list.
"""