"""
Binary search is a divide-and-conquer algorithm used to efficiently search for an element in a sorted array or list. The algorithm works by repeatedly dividing the search interval in half, effectively narrowing down the search space until the target element is found or determined to be absent.
The divide-and-conquer approach used in binary search involves the following steps:
Divide: The sorted array is divided into two halves, with the middle element acting as the pivot.
Conquer: Depending on the comparison between the target element and the pivot, the search is continued in either the left or right half of the array.
Combine: The solution to the original problem is obtained by combining the solutions to the subproblems.
This recursive process continues until the target element is found or the search space is exhausted.

"""
def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target element.

    Args:
        arr (list): A sorted list of elements.
        target (any): The element to search for in the list.

    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    # Test the binary_search function
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
    print(binary_search(sorted_list, 7))  # Output: 3
    print(binary_search(sorted_list, 6))  # Output: -1