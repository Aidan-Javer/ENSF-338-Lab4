def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2
    return li

"""
Question 1:
The best case complexity would be O(n) and this would be the case where every element in the array is less than or equal to 5. This would make it so that the inner loop is never executed and the array is only iterated over once.
The average and worst case complexities are O(n^2) since for every element that is greater than 5, the array is iterated over again. On average, the array will be iterated over at least twice.

Question 2:
The best, average, and worst case complexities are not the same. In the modified version, the complexity of all three cases is O(n^2) since the the array is iterated over twice for each element in the array, regardless of the value of the element. The element is multiplied by 2^n if the element itself is larger than 5.
"""

def processdata_modified(li):
    for i in range(len(li)):
        for j in range(len(li)):
            if li[i] > 5:
                li[i] *= 2
    return li

print(processdata([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(processdata_modified([1, 2, 3, 4, 5, 6, 7, 8, 9]))