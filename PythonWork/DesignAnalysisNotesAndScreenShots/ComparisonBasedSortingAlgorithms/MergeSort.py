"""
Topic Merge Sort

Def:
Merge Sort is a popular and efficient sorting algorithm that follows the divide-and-conquer paradigm.
    It works by recursively breaking down the input array or list into smaller subarrays,
    sorting them, and then merging them back together to obtain the final sorted array.

The key steps in the Merge Sort algorithm are:
Divide: Recursively divide the input array or list
    into two halves until you reach subarrays of size 1.
Conquer: Sort the individual subarrays.
Merge: Merge the sorted subarrays back together to form the final sorted array.

The divide-and-conquer approach of Merge Sort makes it a stable and efficient sorting algorithm,
    with a time complexity of O(n log n), where n is the size of the input.
This makes Merge Sort a great choice for sorting large datasets.

Script Breakdown:
The merge_sort function recursively divides the input array into smaller subarrays,
    sorts them using the merge function,
    and then merges the sorted subarrays back together to obtain the final sorted array.
"""

def merge_sort(arr):
    """
    Recursively sorts the input array using the merge sort algorithm.

    Args:
        arr (list): The input array to be sorted.

    Returns:
        list: The sorted array.
    """
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted arrays into a single sorted array.

    Args:
        left (list): The left sorted subarray.
        right (list): The right sorted subarray.

    Returns:
        list: The merged and sorted array.
    """
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any remaining elements from the left or right subarray
    result += left[left_index:]
    result += right[right_index:]

    return result

if __name__ == '__main__':
    unsorted_list = [5,2,9,1,7,3,8,4,6]
    sorted_list = merge_sort(unsorted_list)
    print(sorted_list)
    #output: [1, 2, 3, 4, 5, 6, 7, 8, 9]