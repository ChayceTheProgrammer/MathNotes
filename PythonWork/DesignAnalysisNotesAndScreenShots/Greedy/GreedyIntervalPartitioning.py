"""
Explanation:
The intervals are sorted by their start time in ascending order:
    [(1, 3), (2, 4), (3, 5), (4, 6), (5, 7)].

The algorithm starts with an empty list of workers.

The first interval (1, 3) is assigned to the first worker.
The second interval (2, 4) does not overlap with the last assigned interval (1, 3) of the first worker,
    so it is assigned to the second worker.
The third interval (3, 5) overlaps with the last assigned interval (1, 3) of the first worker,
    so it is assigned to the first worker.
The fourth interval (4, 6) overlaps with the last assigned interval (2, 4) of the second worker,
    so it is assigned to the second worker.
The fifth interval (5, 7) does not overlap with the last assigned interval (3, 5) of the first worker,
    so it is assigned to the first worker.
The final list of workers is [[(1, 3), (3, 5), (5, 7)], [(2, 4), (4, 6)]].
The key points are:
Sorting the intervals by their start time is the crucial step in the greedy algorithm.
The algorithm assigns each interval to the first worker whose last assigned interval
    ends before the current interval starts.
If no such worker is found, a new worker is created and the current interval is assigned to it.

The time complexity of this algorithm is O(n log n) due to the sorting step, where n is the number
    of intervals.
"""


def interval_partitioning(intervals):
    """
    Solves the interval partitioning problem using a greedy algorithm.

    Args:
        intervals (list): A list of tuples, where each tuple represents an interval
                         with the start and end times.

    Returns:
        list: A list of workers, where each worker is a list of non-overlapping intervals.
    """
    # Sort the intervals by their start time in ascending order
    intervals.sort(key=lambda x: x[0])

    # Initialize the list of workers
    workers = []

    # Iterate through the sorted intervals
    for interval in intervals:
        # Find the first worker whose last assigned interval ends before the current interval starts
        worker_index = next((i for i, w in enumerate(workers) if w[-1][1] <= interval[0]), None)

        # If such a worker is found, assign the current interval to that worker
        if worker_index is not None:
            workers[worker_index].append(interval)
        # Otherwise, create a new worker and assign the current interval to it
        else:
            workers.append([interval])

    return workers

if __name__ == '__main__':
    intervals = [(1, 3), (2, 4), (3, 5), (4, 6), (5, 7)]
    workers = interval_partitioning(intervals)
    print(workers)
    # Output: [[(1, 3), (3, 5), (5, 7)], [(2, 4), (4, 6)]]