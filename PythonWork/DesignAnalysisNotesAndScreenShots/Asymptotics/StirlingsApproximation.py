"""
Stirlings Approximation is a formula
    that gives and approx value for the factoria function: n!

Given by
    n! =/=/= sqrt(2*pi*n) * (n / e)^n
This script will analyze these functions asymptotically and compare differences in their runtime
"""

import math

def factorial(n):
    """
    Calculates the factorial of a given number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def stirling_approximation(n):
    """
    Calculates the Stirling's approximation for the factorial of a given number n.
    """
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n

def compare_growth_rates(n):
    """
    Compares the growth rates of the factorial function and Stirling's approximation.

    Args:
        n (int): The value to use for the comparison.

    Returns:
        A tuple containing the following information:
        - The value of the factorial function n!
        - The value of Stirling's approximation for n!
        - The relative error between the two values
        - The Big-O, Big-Ω, and Big-Θ notations for the factorial function
        - The Big-O, Big-Ω, and Big-Θ notations for Stirling's approximation
    """
    # Calculate the factorial and Stirling's approximation
    n_factorial = factorial(n)
    n_stirling = stirling_approximation(n)

    # Calculate the relative error
    relative_error = abs(n_factorial - n_stirling) / n_factorial

    # Determine the asymptotic growth rates
    # Factorial function n!
    n_factorial_big_o = 'O(n!)'
    n_factorial_big_omega = 'Ω(n!)'
    n_factorial_big_theta = 'Θ(n!)'

    # Stirling's approximation
    n_stirling_big_o = 'O(sqrt(n) * n^n)'
    n_stirling_big_omega = 'Ω(sqrt(n) * n^n)'
    n_stirling_big_theta = 'Θ(sqrt(n) * n^n)'

    return (n_factorial, n_stirling, relative_error,
            n_factorial_big_o, n_factorial_big_omega, n_factorial_big_theta,
            n_stirling_big_o, n_stirling_big_omega, n_stirling_big_theta)

if __name__ == '__main__':

    # Example usage
    n = 20
    result = compare_growth_rates(n)
    print(f"Factorial of {n}: {result[0]}")
    print(f"Stirling's approximation of {n}!: {result[1]}")
    print(f"Relative error: {result[2]:.6f}")
    print()
    print(f"Factorial function n!: {result[3]}, {result[4]}, {result[5]}")
    print(f"Stirling's approximation: {result[6]}, {result[7]}, {result[8]}")