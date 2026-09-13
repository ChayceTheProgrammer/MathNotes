"""
Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum element
    from the unsorted part of the list and swapping it with the first element of the unsorted part.
This process is repeated until the entire list is sorted.
"""

def selection_sort(arr):
    """Sorts the given list in ascending order using Selection Sort."""
    n = len(arr)

    # Traverse through the list
    for i in range(n):
        # Find the minimum element in the unsorted part of the list
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

if __name__ == "__main__":
    unsorted_list = [64, 25, 12, 22, 11]
    sorted_list = selection_sort(unsorted_list)
    print(sorted_list)  # Output: [11, 12, 22, 25, 64]