"""
Overview of Quick Sort

Quick Sort is a popular and efficient sorting algorithm that uses a divide-and-conquer strategy to sort an array or list.
The algorithm works by selecting a 'pivot' element from the array,
    and then partitioning the other elements into two sub-arrays,
    according to whether they are less than or greater than the pivot.

    The sub-arrays are then recursively sorted.

The key steps in the Quick Sort algorithm are:

1. Select a 'pivot' element from the array.
2. Partition the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.
3. Recursively apply the same process to the sub-arrays.

This divide-and-conquer approach makes Quick Sort an efficient algorithm, with an average time complexity of O(n log n).

#### Runtime Analysis

The time complexity of Quick Sort depends on how the pivot element is selected:

- **Best case**: The pivot element is always the median of the array.
    This results in a perfectly balanced partition, and the time complexity is O(n log n).

- **Average case**: The pivot element is randomly selected.
    The time complexity is still O(n log n) on average.

- **Worst case**: The pivot element is always the smallest or largest element in the array. This results in highly unbalanced partitions, and the time complexity degrades to O(n^2).
To avoid the worst case scenario,
    it's common to use a randomized pivot selection or the median-of-three pivot selection strategy.

    These techniques help ensure that the pivot is chosen reasonably well,
    resulting in a balanced partition and maintaining the O(n log n) average time complexity. **


This implementation uses the median-of-three pivot selection strategy, which helps avoid the worst-case scenario. The algorithm recursively sorts the left and right sub-arrays, and then combines the results with the middle (pivot) elements. ****
"""
#Python Implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    # Test the quicksort function
    unsorted_list = [5, 2, 9, 1, 7, 3, 8, 4, 6]
    sorted_list = quicksort(unsorted_list)
    print("Unsorted list:", unsorted_list)
    print("Sorted list:", sorted_list)