"""
This module contains a simple performance test which
compares the recursive version of Floyd's algorithm with the
imperative version.
"""
# Imports
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tests.testgraphs import TEST_GRAPHS
from recursion.recursive_floyd import recursive_floyd as recursive
from iterative.iterative_floyd import iterative_floyd as iterative
from time import process_time

def performance_test():
    """
    A function that performs a simple performance test using process_time.

    Takes no parameters.

    Returns:
    None
    """
    # Designated GRAPH as a global variable
    global GRAPH

    # Number of iterations for process_time
    # Iterations over 10,000 may take a significant amount of time
    iterations = 10_000

    # Test each graph in TEST_GRAPHS
    for graph_name, graph in TEST_GRAPHS.items():
        print(f"\n=== Testing {graph_name} ===")

        # Overwrite the global GRAPH variable with the current graph
        GRAPH = graph

        # Set up MAX_LENGTH for the current graph
        MAX_LENGTH = len(graph)

        # Measure recursive time using process_time
        start_recursive = process_time()
        for i in range(iterations):
            recursive(0, 0, 0)
        end_recursive = process_time()
        total_recursive_time_process = end_recursive - start_recursive

        # Measure iterative time using process_time
        start_iterative = process_time()
        for i in range(iterations):
            iterative()
        end_iterative = process_time()
        total_iterative_time_process = end_iterative - start_iterative

        # Calculate average times per iteration
        avg_recursive_time_process = total_recursive_time_process / iterations
        avg_iterative_time_process = total_iterative_time_process / iterations

        # Print results for this graph
        print(f"\nResults:")
        print(
            f"Recursive Time per Iteration: {avg_recursive_time_process:.8f} seconds")
        print(
            f"Iterative Time per Iteration: {avg_iterative_time_process:.8f} seconds")
        print(
            f"Total Recursive Time: {total_recursive_time_process:.8f} seconds")
        print(
            f"Total Iterative Time: {total_iterative_time_process:.8f} seconds")


# Run performance tests for both implementations side by side for each graphs
if __name__ == "__main__":
    performance_test()
