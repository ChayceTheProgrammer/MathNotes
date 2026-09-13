"""
Explanation:
The max_subarray_sum function uses Kadane's algorithm to find
    the maximum sum of a contiguous subsequence in the given list of numbers.
The function initializes two variables:
    max_sum to keep track of the maximum sum found so far, and
    current_sum to keep track of the maximum sum of the current contiguous subsequence.
The function then iterates through the list of numbers,
    starting from the second element.
For each element,
    the function updates the current_sum
    by taking the maximum of the current element
        and the sum of the current element
        and the previous current_sum.
    This ensures that the current_sum is always the
        maximum sum of a contiguous subsequence ending at the current element.
The function also updates the max_sum by
    taking the maximum of the current max_sum and the current_sum.
    This ensures that max_sum always holds the maximum sum
    of a contiguous subsequence in the entire list.
Finally, the function returns the max_sum,
    which represents the maximum sum
    of a contiguous subsequence in the given list of numbers.

The time complexity of this algorithm is O(n),
    where n is the length of the input list,
    as it only requires a single pass through the list.
"""

def max_subarray_sum(nums):
    """
    Finds the maximum sum of a contiguous subsequence in the given list of numbers.

    Args:
        nums (list): The list of numbers.

    Returns:
        int: The maximum sum of a contiguous subsequence.
    """
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == "__main__":
    # Example usage
    numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray_sum(numbers)
    print("Maximum sum of a contiguous subsequence:", result)