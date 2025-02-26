"""
This module contains a simple performance test which
compares the recursive version of Floyd's algorithm with the
imperative version.
"""

# Imports
# Get parent directory and add to path
import sys
from pathlib import Path
parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))
# Increase recursion limit to allow for larger graph processing
sys.setrecursionlimit(10_000)
from time import process_time # Import process_time for performance testing
# Import recursive and iterative modules and functions
from iterative.iterative_floyd import iterative_floyd as iterative_function
import iterative.iterative_floyd as iterative_module
from recursion.recursive_floyd import recursive_floyd as recursive_function
import recursion.recursive_floyd as recursive_module
from tests.testgraphs import TEST_GRAPHS # Import test graphs


def performance_test(function_handle):
    """
    A function that performs a simple performance test using process_time.

    Parameters: 
    function_handle: The function that is being tested.

    Returns:
    None.
    """
    # Determine which module to use based on the function
    # Otherwise return early
    if function_handle == recursive_function: # pylint: disable=comparison-with-callable
        module = recursive_module
    elif function_handle == iterative_function: # pylint: disable=comparison-with-callable
        module = iterative_module
    else:
        print("Invalid function.")
        return

    # Number of iterations for process_time
    # Iteration count over 100,000 may take a significant amount of time
    iterations = 10_000

    # Iterate through all the test graphs from the
    # TEST_GRAPH dictionary items
    for graph_name, graph in TEST_GRAPHS.items():

        print(f"\n= {graph_name} =")
        total_time = 0 # Initialize timing variable

        # Measure recursive time
        for _ in range(iterations):

            # Reset graph for each iteration by copying it
            # using list comprehension
            module.GRAPH = [row[:] for row in graph]
            module.MAX_LENGTH = len(graph)

            start_time = process_time()  # Start measuring time
            function_handle()  # Call the function
            end_time = process_time()  # Stop measuring time

            # Add up the times
            total_time += (end_time - start_time)

        # Print results for this graph, display to 8 decimal places
        print(f"{total_time:.8f} seconds")

print("\nRecursion Test Time")
# Run the perfomance test on the recursive function
performance_test(recursive_function)

print("\nIterative Test Time")
# Run the perfomance test on the iterative function
performance_test(iterative_function)
