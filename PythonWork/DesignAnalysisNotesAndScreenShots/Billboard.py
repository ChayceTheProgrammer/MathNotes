import math
from decimal import Decimal, getcontext
"""
Key Components:
Generating e digits
We use a simple implementation to generate digits of e
The NASA website was historically used as a source for e digits, but we're generating them 
    programmatically here
    
Primality Testing:
We implement a basic primality test checking up to the square root of the number
This is sufficient since the largest possible 10-digit number is 9,999,999,999

Number Construction:
The algorithm takes consecutive chunks of 10 digits from e
Each chunk is checked for primality until we find the first prime

Historical Context:
This problem was originally part of a Google recruitment campaign When solved, the answer 
    (7427466391) led to a URL that connected to a Google employment page.
    
The algorithm is designed to be efficient by:
a. Using optimized primality testing
b. Only checking numbers that are actually 10 digits long
c. Stopping as soon as the first prime is found
When you run this code, it will output the first 10-digit prime found in consecutive digits of e
"""

def generate_e_digits(precision):
    """Generate digits of e using a more stable method"""
    getcontext().prec = precision + 10  # Set decimal precision

    # Initialize e as Decimal
    e = Decimal(2)
    term = Decimal(1)

    # Generate e using series expansion
    for i in range(2, precision + 10):
        term /= Decimal(i)
        e += term

        if term < Decimal(10) ** (-precision):
            break

    # Convert to string and remove decimal point
    e_str = str(e)
    e_digits = [int(d) for d in e_str.replace('.', '')[:precision]]
    return e_digits


def is_prime(n):
    """Check if a number is prime using trial division"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def find_first_10digit_prime():
    # Generate sufficient digits of e
    e_digits = generate_e_digits(1000)

    # Check consecutive 10-digit numbers
    for i in range(len(e_digits) - 9):
        num = 0
        # Construct 10-digit number
        for j in range(10):
            num = num * 10 + e_digits[i + j]

        # Check if it's a 10-digit number and prime
        if len(str(num)) == 10 and is_prime(num):
            return num


# Run the solution
result = find_first_10digit_prime()
print(f"The first 10-digit prime in e is: {result}")
# should result: 7427466391 as {result}