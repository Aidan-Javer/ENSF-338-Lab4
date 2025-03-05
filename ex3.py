import sys
from matplotlib import pyplot as plt
import timeit

# Part 1: Growth Strategy Explanation (Question 1)
"""
Python's list growth strategy uses an over-allocation formula from lists.c:
new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3; The Growth Factor is 
approximately 12.5%.
"""

# Part 2 ##

def track_capacity_changes(max_elements):
    lst = []
    prev_size = sys.getsizeof(lst)
    last_trigger_size = 0
    for i in range(max_elements):
        lst.append(0)
        current_size = sys.getsizeof(lst)
        if current_size != prev_size:
            print(f"Capacity changed at len={len(lst)} (new sizeof={current_size})")
            last_trigger_size = len(lst) - 1
            prev_size = current_size
    return last_trigger_size 

## Part 3 & 4 ##

if __name__ == "__main__":
    s = track_capacity_changes(64) 
    print(f"Final S where appending causes resize: {s}")

    resize_avg_tm = []
    no_resize_avg_tm = []

    for x in range(1000):
        lst_resize = [0 for x in range(s)]
        lst_no_resize = [0 for x in range(s - 1)]

        resize_times = timeit.timeit(lambda: lst_resize.append(0), number=1)
        no_resize_times = timeit.timeit(lambda: lst_no_resize.append(0), number=1)

        resize_avg_tm.append(resize_times)
        no_resize_avg_tm.append(no_resize_times)

    print(f"Avg resize time (S->S+1): {sum(resize_avg_tm)/len(resize_avg_tm):.8f} sec")
    print(f"Avg no-resize time (S-1->S): {sum(no_resize_avg_tm)/len(no_resize_avg_tm):.8f} sec")


## Part 5 ##

    plt.hist(resize_avg_tm, bins="auto", edgecolor="black", alpha=0.5, label='Resize (S -> S+1)')
    plt.hist(no_resize_avg_tm, bins="auto", alpha=0.5, edgecolor="black", label='No Resize (S-1 -> S)')
    plt.xlim(0, 0.00001)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Frequency")
    plt.title("Append Operation Time Distribution")
    plt.legend()
    plt.show()
"""
Going from a list size of S -> S + 1 takes longer than S - 1 -> S because the first operation involves the deallocation and reallocation
of new memory, whereas the second operation requires adding/appending the new element without having to resize the list. Thus, the first 
is a O(n) operation whereas, the second is an O(1)
"""
