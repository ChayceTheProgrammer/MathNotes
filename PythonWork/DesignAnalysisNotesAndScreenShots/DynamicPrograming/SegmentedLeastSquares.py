"""
Explanation:
The segmented_least_squares function takes the independent variable x,
    the dependent variable y, and the number of segments num_segments as input.
The function initializes the segment boundaries by dividing the range of x values
    into num_segments + 1 equally spaced points.
The objective function to be minimized is defined as the sum of squares of the
    residuals between the actual y values and the fitted values.
The minimize function from the scipy.optimize module is used to optimize
    the segment parameters (slopes and intercepts) to minimize the objective function.
The fitted values, slopes, intercepts, and segment boundaries are then extracted and returned.

The key points are:
Segmented least squares is a technique that fits multiple linear segments to the data,
    rather than a single linear function.
The algorithm determines the optimal number and boundaries of the segments to minimize the overall error.

The fitted values, slopes, intercepts, and segment boundaries are returned as the output of the function.
"""
import numpy as np
from scipy.optimize import minimize


def segmented_least_squares(x, y, num_segments):
    """
    Performs segmented least squares on the given data.

    Args:
        x (numpy.ndarray): The independent variable (x-coordinates).
        y (numpy.ndarray): The dependent variable (y-coordinates).
        num_segments (int): The number of segments to use.

    Returns:
        numpy.ndarray: The fitted values for the dependent variable.
        numpy.ndarray: The slopes of the linear segments.
        numpy.ndarray: The intercepts of the linear segments.
        numpy.ndarray: The boundaries of the segments.
    """
    n = len(x)

    # Initialize the segment boundaries
    segment_boundaries = np.linspace(0, n, num_segments + 1, dtype=int)

    # Define the objective function to minimize
    def objective_function(params):
        fitted_y = np.zeros_like(y)
        for i in range(num_segments):
            start = segment_boundaries[i]
            end = segment_boundaries[i + 1]
            slope = params[i]
            intercept = params[num_segments + i]
            fitted_y[start:end] = slope * x[start:end] + intercept
        return np.sum((y - fitted_y) ** 2)

    # Optimize the segment parameters
    initial_params = np.zeros(2 * num_segments)
    res = minimize(objective_function, initial_params, method='L-BFGS-B')

    # Extract the fitted parameters
    slopes = res.x[:num_segments]
    intercepts = res.x[num_segments:]

    # Compute the fitted values
    fitted_y = np.zeros_like(y)
    for i in range(num_segments):
        start = segment_boundaries[i]
        end = segment_boundaries[i + 1]
        fitted_y[start:end] = slopes[i] * x[start:end] + intercepts[i]

    return fitted_y, slopes, intercepts, segment_boundaries

if __name__ == '__main__':
    # Generate some sample data
    x = np.linspace(0, 10, 100)
    y = 2 * x + 5 + np.random.normal(0, 2, 100)
    y[50:70] = 4 * x[50:70] - 10 + np.random.normal(0, 2, 20)

    # Perform segmented least squares
    num_segments = 2
    fitted_y, slopes, intercepts, segment_boundaries = segmented_least_squares(x, y, num_segments)

    # Print the results
    print("x-values: ", x)
    print("Fitted values:", fitted_y)
    print("Slopes:", slopes)
    print("Intercepts:", intercepts)
    print("Segment boundaries:", segment_boundaries)