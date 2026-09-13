"""
#### Introduction to Bubble Sort

Bubble Sort is a simple comparison-based sorting algorithm
    that works by repeatedly swapping adjacent elements if they are in the wrong order.
    The algorithm gets its name from the way smaller elements "bubble up" to the top of the list as the algorithm progresses.

Bubble Sort is one of the easiest sorting algorithms to understand and implement,
    making it a great starting point for learning about sorting algorithms.
    However, it is generally not efficient for large data sets,
    as its average and worst-case time complexity are quite high.

The `bubble_sort` function takes a list `arr` as input and returns the sorted list.
    The algorithm works by iterating through the list,
    comparing adjacent elements and swapping them if they are in the wrong order.
    This process is repeated until the list is fully sorted.

The outer loop runs `n` times, where `n` is the length of the input list.
The inner loop runs `n-i-1` times, where `i` is the current iteration of the outer loop.
This is because the last `i` elements are already in their correct positions and don't need to be checked.

The time complexity of Bubble Sort is O(n^2) in the average and worst cases,
    making it inefficient for large data sets.
However, it is a simple and easy-to-understand algorithm,
making it a good choice for small lists or as an educational tool.
"""


def bubble_sort(arr):
    """
    Sorts the given list in ascending order using the Bubble Sort algorithm.

    Args:
        arr (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(arr)

    # Traverse through all list elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

if __name__ == "__main__":
    """
    The main function that can be executed when the script is run directly.
    """
    # Example usage
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubble_sort(unsorted_list)
    print("Sorted list:", sorted_list)