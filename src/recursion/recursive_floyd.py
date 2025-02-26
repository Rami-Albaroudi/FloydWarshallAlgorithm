"""
This module has a simple implementation of Floyd's Algorithm
It contains three main functions:
    main -> controls the execution of the script
    print_out_graph -> prints out the graph with nodes and distances
    recursive_floyd -> computes shortest path

The global variables are:
    NO_PATH = Marker for where there is no path. This is the max value of an integer
    GRAPH = Contains the distances for the graph. Node names are inferred by the position
    of the node, i.e. position  0 0 in the list is node 0
    MAX_LENGTH = The size of the graph
    MIN_LEVEL = The lowest search level for the shortest path calculation
    NO_PATH_MARKER = Holder for no path possible. This is used for the printing function. 
"""
# Imports
from sys import maxsize
NO_PATH = maxsize
GRAPH = [[0,   7,  NO_PATH, 8],
         [NO_PATH,  0,  5,  NO_PATH],
         [NO_PATH, NO_PATH, 0,   2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(GRAPH[0])
MIN_LEVEL = 0
NO_PATH_MARKER = "No Path"


def main():
    """
    This is the calling function for the recursive floyd's algorithm
    """

    recursive_floyd()
    print_out_graph()


def print_out_graph():
    """
    This function prints out the graph with the distances
    and a place holder for no path between nodes
    """
    for start_node in range(0, MAX_LENGTH):
        for end_node in range(0, MAX_LENGTH):
            distance = GRAPH[start_node][end_node]
            if distance == NO_PATH:
                distance = NO_PATH_MARKER

            # Converted to f string
            message = (
                f"Distance from Node {start_node} to Node {end_node} is {distance}")
            print(message)


def recursive_floyd(outer_loop: int = 0, middle_loop: int = 0, inner_loop: int = 0):
    """
    This function computes shortest path between each pair of nodes recursively.
    It compares direct paths with paths that pass through intermediate nodes.

    param: outer_loop: Represents the current intermediate node being considered.
    param: middle_loop: Represents the current source node.
    param: inner_loop: Represents the current destination node.
    """
    # Base case: If all intermediate nodes have been processed
    if outer_loop >= MAX_LENGTH:
        return

    # Handle self-loops: Set diagonal elements to 0
    if middle_loop == inner_loop:
        GRAPH[middle_loop][inner_loop] = 0
    else:
        # Update the distance if a shorter path is found through the intermediate node
        if GRAPH[middle_loop][outer_loop] != NO_PATH and GRAPH[outer_loop][inner_loop] != NO_PATH:
            GRAPH[middle_loop][inner_loop] = min(
                GRAPH[middle_loop][inner_loop],
                GRAPH[middle_loop][outer_loop] +
                GRAPH[outer_loop][inner_loop]
            )

    # Recursive calls to handle different cases
    if inner_loop < MAX_LENGTH - 1:
        # Move to the next destination node
        recursive_floyd(outer_loop, middle_loop, inner_loop + 1)
    elif middle_loop < MAX_LENGTH - 1:
        # Move to the next source node, reset destination node
        recursive_floyd(outer_loop, middle_loop + 1, 0)
    else:
        # Move to the next intermediate node, reset source and destination nodes
        recursive_floyd(outer_loop + 1, 0, 0)


if __name__ == "__main__":
    main()
