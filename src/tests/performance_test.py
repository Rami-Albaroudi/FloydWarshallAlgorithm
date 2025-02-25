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
    function_handle: The function that is being tested

    Returns:
    None
    """
    # Determine which module to use based on the function
    if function_handle == recursive_function:
        module = recursive_module
    elif function_handle == iterative_function:
        module = iterative_module
    else:
        return print("Invalid function.")
    
    # Number of iterations for process_time
    # Iteration count over 100,000 may take a significant amount of time
    iterations = 100_000

    # Test each graph in TEST_GRAPHS
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
performance_test(recursive_function)

print("\nIterative Test Time")
performance_test(iterative_function)
