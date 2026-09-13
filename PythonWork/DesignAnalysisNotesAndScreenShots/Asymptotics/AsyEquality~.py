import math


def f(x):
    """
    A function that grows asymptotically as O(x^2).
    """
    return x ** 2 + 3 * x


def g(x):
    """
    A function that also grows asymptotically as O(x^2).
    """
    return x ** 2 + 1


def are_asymptotically_equal(f, g, x):
    """
    Checks if two functions f(x) and g(x) are asymptotically equal as x goes to infinity.

    Args:
        f (function): The first function to compare.
        g (function): The second function to compare.
        x (float): The value of x to use for the comparison.

    Returns:
        bool: True if the functions are asymptotically equal, False otherwise.
    """
    limit = (f(x) / g(x))
    return abs(limit - 1) < 1e-4


if __name__ == "__main__":
    # Example usage
    for x in [10, 100, 1000, 10000, 100000, 1000000, 100000000000]:
        print(f"For x = {x}:")
        print(f"f(x) = {f(x)}")
        print(f"g(x) = {g(x)}")
        if are_asymptotically_equal(f, g, x):
            print("The functions are asymptotically equal.")
        else:
            print("The functions are not asymptotically equal.")
        print()

"""
Sample Output:
For x = 10:
f(x) = 130
g(x) = 101
The functions are not asymptotically equal.

For x = 100:
f(x) = 10300
g(x) = 10001
The functions are not asymptotically equal.

For x = 1000:
f(x) = 1003000
g(x) = 1000001
The functions are not asymptotically equal.

For x = 10000:
f(x) = 100030000
g(x) = 100000001
The functions are not asymptotically equal.

For x = 100000:
f(x) = 10000300000
g(x) = 10000000001
The functions are asymptotically equal.

For x = 1000000:
f(x) = 1000003000000
g(x) = 1000000000001
The functions are asymptotically equal.

For x = 100000000000:
f(x) = 10000000000300000000000
g(x) = 10000000000000000000001
The functions are asymptotically equal.
"""