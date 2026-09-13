import math

def harmonic_number(n):
    """Calculates the nth harmonic number."""
    return sum(1/i for i in range(1, n+1))

def main():
    n = 100000  # Choose a large value of n
    #precompute h_n to save resources
    h_n = harmonic_number(n)
    ln = math.log(n)
    print(f"The {n}th harmonic number is: {h_n:.6f}")
    print(f"The natural logarithm of {n} is: {ln:.6f}")
    print(f"The difference between the two is: {h_n - ln:.6f}")

    #The difference between h_n and ln(n) approaches a constant as n increases
    #this constant is about: .557216 when n is 100000000
    #(also called the Euler-Mascheroni constant, γ)
    #thus they are asymptotically equivalent

if __name__ == "__main__":
    main()