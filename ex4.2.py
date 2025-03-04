def linear_search(arr, val):    # Inefficient linear search
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1

def binary_search(arr, low, high, val):     # Efficient binary search
    while low <= high:
        mid = (low + high) // 2
        if val == arr[mid]:
            return mid
        elif val > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

"""
Question 4:
The worst case complexity for linear search is O(n) and occurs when the value of interest is the last element of the array or does not exist in the array. 
The worst case complexity for binary search is O(log(n)) and occurs when the value of interest is either the first or the last element of the array, or does not exist in the array.
"""
import timeit
from matplotlib import pyplot as plt

num_list = [x for x in range(1000)]
list_lengths = range(1000, 26000, 1000)
linear_avg_times = []
binary_avg_times = []
for i in list_lengths:
    num_list = list(range(i))
    val = len(num_list) - 1
    linear_times = []
    binary_times = []
    for j in range(100):
        linear_tm = timeit.timeit(lambda: linear_search(num_list, val), number = 1)
        linear_times.append(linear_tm)

        binary_tm = timeit.timeit(lambda: binary_search(num_list, 0, len(num_list) - 1, val), number = 1)
        binary_times.append(binary_tm)

    linear_avg_times.append(sum(linear_times) / len(linear_times))
    binary_avg_times.append(sum(binary_times) / len(binary_times))

plt.figure(figsize=(9, 7))
plt.scatter(list_lengths, linear_avg_times, color='r', label="Linear Search")
plt.scatter(list_lengths, binary_avg_times, color='b', label="Binary Search")
plt.legend()
plt.title("Time Required to Search for Last Element in Array")
plt.ylabel("Time required (s)")
plt.xlabel("Array size")
plt.savefig("ex4.2.png")
