import timeit

#Definitons and Pre-Amble
"""
Big-Θ (alt+233)
    used like Θ( f(n) ) means the function's growth rate is bounded
    ABOVE and BELOW by constant multiples of f(n)
    --> Tight Bound
    [same asymptotic growth rate means being in the same Θ class]
    Found By:
    
Big-O:
    used like O (f(n) ) to say the function's growth rate is bounded ABOVE
    by a constant multiple of f(n)
    -->Upper Bound
    
    
Big-Ω (alt+234)
    used like Ω( f(n) ) to say to the function's growth rate is bounded BELOW
    by a constant multiple of f(n)
    -->Lower Bound
    [cares about the lowest order term that provides the LowBound for function]
    
    Big Theta (Θ) represents the tightest bound that encompasses both 
        the upper bound (Big O) and the lower bound (Big Omega).
    If the upper bound (Big O) and the lower bound (Big Omega) are the same, 
        then the Big Theta (Θ) bound is also the same.
    For example, if f(n) = O(n^2) and f(n) = Ω(n^2), then f(n) = Θ(n^2).
    
    
Equality: ~
    means that the ratio of the two functions approaches 1 as n goes to infinity:
    ->  lim ( f(n) / g(n) ) = 1
    This is a STRICT condition and tells us they have the same
        Leading term in their growth.
"""

def compare_functions(f, g, input_size):
    """
    Compares the runtime of two functions f and g for a given input size.

    Args:
        f (function): The first function to compare.
        g (function): The second function to compare.
        input_size (int): The size of the input to use for the comparison.

    Returns:
        A tuple containing the runtime analysis of the two functions.
        The first element is the runtime analysis of f(x), and the second
        element is the runtime analysis of g(x).
    """
    f_runtime = timeit.timeit(f'f({input_size})', globals=globals(), number=1000)
    g_runtime = timeit.timeit(f'g({input_size})', globals=globals(), number=1000)

    # Determine the Big-O, Big-Ω, and Big-Θ for each function
    f_big_o = 'O(x^2)'
    f_big_omega = 'Ω(x)'
    f_big_theta = 'Θ(x^2)'

    g_big_o = 'O(x^2)'
    g_big_omega = 'Ω(x^2)'
    g_big_theta = 'Θ(x^2)'

    return (f'f(x): {f_big_o}, {f_big_omega}, {f_big_theta}', f'g(x): {g_big_o}, {g_big_omega}, {g_big_theta}')

#example of asymptotic analysis
def f(x):
    """
    Big-O -> O(n^2) [Upper]
        reason: n^2 dominates over 3x as n gets large
    Big-Ω -> Ω(n) [Lower]
        reason: 3x is the lowest order term
    Thus:
        Big-Θ -> Θ(n^2) [Tight]
            reason: The function is both upper and lower bounded by constant multiples of x^2
            The upper bound is O(x^2), and the lower bound is Ω(x).
            The tightest bound that encompasses both is Θ(x^2), as the term x^2 dominates the function's growth.
    """

    return x**2 + 3*x

def g(x):
    """
    Analysis:
        The upper bound is O(x^2), and the lower bound is Ω(x^2).
        The tightest bound that encompasses both is Θ(x^2),
        as the term x^2 is the dominant term in the function's growth.
    g(x) = O(x^2)  (Upper Bound)
    g(x) = Ω(x^2)  (Lower Bound)
    """
    return x**2

if __name__ == "__main__":
        print(f"f-runtime: {timeit.timeit('f(100)', globals=globals(), number=1000)}")
        print(f"g-runtime: {timeit.timeit('g(100)', globals=globals(), number=1000)}")
        print(compare_functions(f, g, 100))