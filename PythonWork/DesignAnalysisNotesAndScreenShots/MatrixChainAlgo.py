"""
This script goes over the optimal matrix chain algorithm
"""

def matrix_chain_multiplication(dimensions):
    n = len(dimensions) - 1

    # Initialize the cost and parenthesization tables
    cost = [[0 for _ in range(n)] for _ in range(n)]
    parenthesization = [[0 for _ in range(n)] for _ in range(n)]

    # Fill the tables using dynamic programming
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')
            for k in range(i, j):
                temp_cost = cost[i][k] + cost[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if temp_cost < cost[i][j]:
                    cost[i][j] = temp_cost
                    parenthesization[i][j] = k

    # Reconstruct the optimal parenthesization
    def print_parenthesization(i, j):
        if i == j:
            print(f"M{i+1}", end="")
        else:
            print("(", end="")
            print_parenthesization(i, parenthesization[i][j])
            print_parenthesization(parenthesization[i][j] + 1, j)
            print(")", end="")

    print("Optimal Parenthesization:")
    print_parenthesization(0, n - 1)
    print()
    print(f"Minimum Cost: {cost[0][n-1]}")

# Test case (from hw5q2)
sample_dimensions = [5, 10, 3, 12, 5, 50, 6]
matrix_chain_multiplication(sample_dimensions)