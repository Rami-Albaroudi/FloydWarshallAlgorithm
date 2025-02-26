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
# Import implementations
from recursion.recursive_floyd import recursive_floyd as recursive_function
import recursion.recursive_floyd as recursive_module
from iterative.iterative_floyd import iterative_floyd as iterative_function
import iterative.iterative_floyd as iterative_module
from tests.testgraphs import UNITTEST_GRAPHS, UNITTEST_GRAPHS_EXPECTED

class FloydWarshallTest(unittest.TestCase):
    """Test class for Floyd-Warshall algorithm implementations."""
    
    def test_recursive_implementation(self):
        """Test the recursive implementation against expected outputs."""
        for graph_name, graph in UNITTEST_GRAPHS.items():
            with self.subTest(graph=graph_name):
                # Set up and run
                recursive_module.GRAPH = [row[:] for row in graph]
                recursive_module.MAX_LENGTH = len(graph)
                recursive_function()
                
                # Assert
                self.assertEqual(
                    recursive_module.GRAPH, 
                    UNITTEST_GRAPHS_EXPECTED[graph_name],
                    f"Failed on {graph_name}"
                )
        
    def test_iterative_implementation(self):
        """Test the iterative implementation against expected outputs."""
        for graph_name, graph in UNITTEST_GRAPHS.items():
            with self.subTest(graph=graph_name):
                # Set up and run
                iterative_module.GRAPH = [row[:] for row in graph]
                iterative_module.MAX_LENGTH = len(graph)
                iterative_function()
                
                # Assert
                self.assertEqual(
                    iterative_module.GRAPH, 
                    UNITTEST_GRAPHS_EXPECTED[graph_name],
                    f"Failed on {graph_name}"
                )
    
    def test_implementations_match(self):
        """Test that both implementations produce identical results."""
        for graph_name, graph in UNITTEST_GRAPHS.items():
            with self.subTest(graph=graph_name):

                # Run recursive
                recursive_module.GRAPH = [row[:] for row in graph]
                recursive_module.MAX_LENGTH = len(graph)
                recursive_function()
                recursive_result = [row[:] for row in recursive_module.GRAPH]
                
                # Run iterative
                iterative_module.GRAPH = [row[:] for row in graph]
                iterative_module.MAX_LENGTH = len(graph)
                iterative_function()
                iterative_result = [row[:] for row in iterative_module.GRAPH]
                
                # Compare results
                self.assertEqual(recursive_result, iterative_result)

if __name__ == "__main__":
    unittest.main()
