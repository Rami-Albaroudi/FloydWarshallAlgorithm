"""
This module contains a simple performance test which
compares the recursive version of Floyd's algorithm with the
imperative version.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import timeit
from time import process_time
from iterative.iterative_floyd import iterative_floyd as iterative
from recursion.recursive_floyd import recursive_floyd as recursive
from tests.testgraphs import TEST_GRAPHS


def performance_test():
    """
    A function that performs a simple performance test using both timeit and process_time.

    Returns:
    None
    """
    global GRAPH

    # Number of iterations for timeit and process_time
    iterations = 100_000

    # Test each graph in TEST_GRAPHS
    for graph_name, graph in TEST_GRAPHS.items():
        print(f"\n=== Testing {graph_name} Graph ===")

        # Overwrite the global GRAPH variable with the current graph
        GRAPH = graph

        # Set up MAX_LENGTH for the current graph
        MAX_LENGTH = len(graph)

        # --- Measure Time Using timeit ---
        # Measure recursive time using timeit
        recursive_time_timeit = timeit.timeit(
            lambda: recursive(0, 0, 0),
            number=iterations  # Run the function n times
        )

        # Measure iterative time using timeit
        iterative_time_timeit = timeit.timeit(
            lambda: iterative(),
            number=iterations  # Run the function n times
        )

        # --- Measure Time Using process_time ---
        # Measure recursive time using process_time
        start_recursive = process_time()
        for iteration in range(iterations):
            recursive(0, 0, 0)
        end_recursive = process_time()
        total_recursive_time_process = end_recursive - start_recursive

        # Measure iterative time using process_time
        start_iterative = process_time()
        for iteration in range(iterations):
            iterative()
        end_iterative = process_time()
        total_iterative_time_process = end_iterative - start_iterative

        # Calculate average times per iteration for both methods
        avg_recursive_time_timeit = recursive_time_timeit / iterations
        avg_iterative_time_timeit = iterative_time_timeit / iterations

        avg_recursive_time_process = total_recursive_time_process / iterations
        avg_iterative_time_process = total_iterative_time_process / iterations

        # Print results for this graph
        print(f"--- Timeit Results ---")
        print(f"Recursive Time per Iteration (timeit): {avg_recursive_time_timeit:.8f} seconds")
        print(f"Iterative Time per Iteration (timeit): {avg_iterative_time_timeit:.8f} seconds")
        print(f"Total Recursive Time (timeit): {recursive_time_timeit:.8f} seconds")
        print(f"Total Iterative Time (timeit): {iterative_time_timeit:.8f} seconds")

        print(f"\n--- Process Time Results ---")
        print(f"Recursive Time per Iteration (process): {avg_recursive_time_process:.8f} seconds")
        print(f"Iterative Time per Iteration (process): {avg_iterative_time_process:.8f} seconds")
        print(f"Total Recursive Time (process): {total_recursive_time_process:.8f} seconds")
        print(f"Total Iterative Time (process): {total_iterative_time_process:.8f} seconds")


# Run performance tests for both implementations side by side for each graphs
if __name__ == "__main__":
    performance_test()

