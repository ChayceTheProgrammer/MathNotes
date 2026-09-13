"""
The interval scheduling problem can be solved using a greedy algorithm.
The goal is to select the maximum number of non-overlapping intervals from a given set of intervals.
Algorithm:
Sort the intervals by their finish time in ascending order.
Initialize an empty set to store the selected intervals.
Iterate through the sorted intervals:
If the current interval does not overlap with the last selected interval, add it to the set.
Otherwise, skip the current interval and move to the next one.
Return the set of selected intervals.

Explanation:
The intervals are sorted by their finish time in ascending order:
    [(1, 3), (2, 4), (3, 5), (4, 6), (5, 7)].
The algorithm starts with an empty set of selected intervals.
The first interval (1, 3) is added to the set of selected intervals.
The second interval (2, 4) overlaps with the last selected interval (1, 3), so it is skipped.
The third interval (3, 5) does not overlap with the last selected interval (1, 3),
    so it is added to the set of selected intervals.
The fourth interval (4, 6) overlaps with the last selected interval (3, 5), so it is skipped.
The fifth interval (5, 7) does not overlap with the last selected interval (3, 5),
    so it is added to the set of selected intervals.
The final set of selected intervals is [(1, 3), (3, 5), (5, 7)].


The key points are:
Sorting the intervals by their finish time is the crucial step in the greedy algorithm.
The algorithm selects the intervals that do not overlap with the previously selected intervals.
The time complexity of this algorithm is O(n log n) due to the sorting step,
    where n is the number of intervals.
"""


def interval_scheduling(intervals):
    """
    Solves the interval scheduling problem using a greedy algorithm.

    Args:
        intervals (list): A list of tuples, where each tuple represents an interval
                         with the start and end times.

    Returns:
        list: A list of selected intervals.
    """
    # Sort the intervals by their finish time in ascending order
    intervals.sort(key=lambda x: x[1])

    # Initialize the set of selected intervals
    selected = []

    # Iterate through the sorted intervals
    for interval in intervals:
        # If the current interval does not overlap with the last selected interval,
        # add it to the set of selected intervals
        if not selected or interval[0] >= selected[-1][1]:
            selected.append(interval)

    return selected

#testing
if __name__ == '__main__':
    intervals = [(1, 3), (2, 4), (3, 5), (4, 6), (5, 7)]
    selected_intervals = interval_scheduling(intervals)
    print(selected_intervals)  # Output: [(1, 3), (3, 5), (5, 7)]