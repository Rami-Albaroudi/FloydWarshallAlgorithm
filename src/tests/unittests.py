"""
Unit tests for the Floyd-Warshall algorithm implementations.
"""
# Imports
import unittest
from pathlib import Path
import sys
parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))
# Increase recursion limit to allow for larger graph processing
sys.setrecursionlimit(10_000)
# Import recursive and iterative modules and functions
from recursion.recursive_floyd import recursive_floyd as recursive_function
import recursion.recursive_floyd as recursive_module
from iterative.iterative_floyd import iterative_floyd as iterative_function
import iterative.iterative_floyd as iterative_module
# Import test graphs and their expected outputs
from tests.testgraphs import TEST_GRAPHS, TEST_GRAPHS_EXPECTED

class FloydWarshallTest(unittest.TestCase):
    """Test class for Floyd-Warshall algorithm function tests."""

    def test_recursive_function(self):
        """Test the recursive function against expected outputs."""

        # Iterate through all the test graphs from the
        # TEST_GRAPH dictionary items
        for graph_name, graph in TEST_GRAPHS.items():

            # Set up and run test
            with self.subTest(graph=graph_name):

                # Reset graph for each iteration by copying it
                # using list comprehension
                recursive_module.GRAPH = [row[:] for row in graph]
                recursive_module.MAX_LENGTH = len(graph)

                recursive_function() # Call the recursive function

                # Assert that the module's graph is equal to
                # the expected graph after the function is finished
                self.assertEqual(
                    recursive_module.GRAPH,
                    TEST_GRAPHS_EXPECTED[graph_name],
                    f"Failed on {graph_name}"
                )

    def test_iterative_function(self):
        """Test the iterative function against expected outputs."""

        # Iterate through all the test graphs from the
        # TEST_GRAPH dictionary items
        for graph_name, graph in TEST_GRAPHS.items():

            # Set up and run test
            with self.subTest(graph=graph_name):

                # Reset graph for each iteration by copying it
                # using list comprehension
                iterative_module.GRAPH = [row[:] for row in graph]
                iterative_module.MAX_LENGTH = len(graph)

                iterative_function() # Call the iterative function

                # Assert that the module's graph is equal to
                # the expected graph after the function is finished
                self.assertEqual(
                    iterative_module.GRAPH,
                    TEST_GRAPHS_EXPECTED[graph_name],
                    f"Failed on {graph_name}"
                )

    def test_functions_match(self):
        """
        Test that both functions produce identical 
        results for the same graph.
        """

        # Iterate through all the test graphs from the
        # TEST_GRAPH dictionary items
        for graph_name, graph in TEST_GRAPHS.items():

            # Set up and run test
            with self.subTest(graph=graph_name):

                # Reset graph for each iteration by copying it
                # using list comprehension
                recursive_module.GRAPH = [row[:] for row in graph]
                recursive_module.MAX_LENGTH = len(graph)

                # Call the recursive function and store the output graph
                # for comparison, since it will get overwritten by the
                # next function call
                recursive_function()
                recursive_result = [row[:] for row in recursive_module.GRAPH]

                # Reset graph for each iteration by copying it
                # using list comprehension
                iterative_module.GRAPH = [row[:] for row in graph]
                iterative_module.MAX_LENGTH = len(graph)

                # Call the iterative function and store the output graph
                # for comparison, since it will get overwritten by the
                # next function call
                iterative_function()
                iterative_result = [row[:] for row in iterative_module.GRAPH]

                # Assert that the output graphs produced by
                # both functions are the same for each input graph
                self.assertEqual(recursive_result, iterative_result)

# Unit test main method required to run as module
if __name__ == "__main__":
    unittest.main()
