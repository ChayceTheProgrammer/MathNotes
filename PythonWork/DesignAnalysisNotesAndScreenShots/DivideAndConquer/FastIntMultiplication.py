"""
Overview of the Algorithm
The Karatsuba algorithm is a fast integer multiplication algorithm
    that uses a divide-and-conquer approach to reduce the number of multiplications required.
    It was developed by Anatoly Karatsuba in 1960 and is an improvement over the standard long multiplication algorithm.

The key idea behind the Karatsuba algorithm is to break down
    the multiplication of two large integers into a series of smaller multiplications and additions.
    This allows for a significant reduction in the number of operations required, leading to a faster runtime.

The runtime complexity of the Karatsuba algorithm is O(n^(log2 3)), which is approximately O(n^1.585).
This is a significant improvement over the standard long multiplication algorithm, which has a runtime complexity of O(n^2).
The Karatsuba algorithm uses the divide-and-conquer paradigm
"""

def karatsuba(x, y):
    """
    Implement the Karatsuba algorithm for fast integer multiplication.
    """
    if x < 10 or y < 10:
        return x * y

    # Split the digits of the numbers in the middle
    n = max(len(str(x)), len(str(y)))
    n2 = n // 2

    a = x // 10**(n2)
    b = x % 10**(n2)
    c = y // 10**(n2)
    d = y % 10**(n2)

    # Recursively calculate the products
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

    # Combine the results to get the final product
    return ac * 10**(2*n2) + (ad_plus_bc * 10**n2) + bd

if __name__ == '__main__':
    x = 192032438120
    y = 10823317
    print(karatsuba(x, y))