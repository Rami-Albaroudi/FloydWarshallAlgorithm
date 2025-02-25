"""
This module contains a simple performance test which
compares the recursive version of Floyd's algorithm with the
imperative version.
"""
# Imports
from pathlib import Path
# Get parent directory and add to path
parent_dir = Path(__file__).parent.parent
import sys
sys.path.append(str(parent_dir))
# Import test graphs
from tests.testgraphs import TEST_GRAPHS
# Import recursive and iterative modules and functions
import recursion.recursive_floyd as recursive_module
from recursion.recursive_floyd import recursive_floyd as recursive_function
import iterative.iterative_floyd as iterative_module
from iterative.iterative_floyd import iterative_floyd as iterative_function
# Import process_time for performance testing
from time import process_time

def performance_test():
    """
    A function that performs a simple performance test using process_time.

    Takes no parameters.

    Returns:
    None
    """

    # Number of iterations for process_time
    # Iterations over 10,000 may take a significant amount of time
    iterations = 100_000

    # Test each graph in TEST_GRAPHS
    for graph_name, graph in TEST_GRAPHS.items():
        print(f"\n=== Testing {graph_name} ===")

        # Measure recursive time
        start_recursive = process_time()
        for i in range(iterations):
            # Reset graph for each iteration using list comprehension
            recursive_module.GRAPH = [row[:] for row in graph]
            recursive_module.MAX_LENGTH = len(graph)
            recursive_function()
        end_recursive = process_time()
        total_recursive_time = end_recursive - start_recursive

        # Measure iterative time
        start_iterative = process_time()
        for i in range(iterations):
            # Reset graph for each iteration using list comprehension
            iterative_module.GRAPH = [row[:] for row in graph]
            iterative_module.MAX_LENGTH = len(graph)
            iterative_function()
        end_iterative = process_time()
        total_iterative_time = end_iterative - start_iterative

        # Calculate average times per iteration
        avg_recursive_time = total_recursive_time / iterations
        avg_iterative_time = total_iterative_time / iterations

        # Print results for this graph
        print(f"\nResults:")
        print(
            f"Recursive Time per Iteration: {avg_recursive_time:.8f} seconds")
        print(
            f"Iterative Time per Iteration: {avg_iterative_time:.8f} seconds")
        print(
            f"Total Recursive Time: {total_recursive_time:.8f} seconds")
        print(
            f"Total Iterative Time: {total_iterative_time:.8f} seconds")


# Run performance tests for both implementations side by side for each graphs
if __name__ == "__main__":
    performance_test()
