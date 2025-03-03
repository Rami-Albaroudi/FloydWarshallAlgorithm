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


def recursive_floyd(outer_loop: int = MIN_LEVEL,
                    middle_loop: int = MIN_LEVEL,
                    inner_loop: int = MIN_LEVEL):
    """
    Recursively finds the shortest path between all pairs of 
    nodes using Floyd-Warshall algorithm.
    
    This function uses recursion to process each combination of 
    intermediate, source, and destination nodes. It checks if a 
    path through the intermediate node is shorter than the current direct path.

    Parameters:
    outer_loop (int): Current intermediate node (k) being considered for path improvement.
    middle_loop (int): Current source node (i) from which paths originate.
    inner_loop (int): Current destination node (j) to which paths lead.
    All the params are set to MIN_LEVEL (0) since we are starting the search at the
    lowest level.

    Returns:
    None: Updates the global GRAPH in-place with shortest path distances.
    """

    # Base case: Algorithm completion when all
    # intermediate nodes have been processed
    if outer_loop >= MAX_LENGTH:
        return

    # Handle self-loops: Distance from a node to itself is always 0
    if middle_loop == inner_loop:
        GRAPH[middle_loop][inner_loop] = 0
    else:
        # Only consider paths where both segments source to intermediate
        # and intermediiate to destination exist
        if GRAPH[middle_loop][outer_loop] != NO_PATH and GRAPH[outer_loop][inner_loop] != NO_PATH:
            # Calculate potential new path length through current intermediate node
            GRAPH[middle_loop][inner_loop] = min(
                GRAPH[middle_loop][inner_loop],
                GRAPH[middle_loop][outer_loop] +
                GRAPH[outer_loop][inner_loop]
            )

    # Recursive calls to handle different cases
    if inner_loop < MAX_LENGTH - 1:
         # Process next destination node while keeping
         # same source and intermediate nodes
        recursive_floyd(outer_loop, middle_loop, inner_loop + 1)
    elif middle_loop < MAX_LENGTH - 1:
        # Process next source node and reset destination node
        # while keeping same intermediate node
        recursive_floyd(outer_loop, middle_loop + 1, 0)
    else:
        # Process next intermediate node and reset
        # both source and destination nodes
        # This make sure it fully processes each intermediate node
        # before moving to the next
        recursive_floyd(outer_loop + 1, 0, 0)


if __name__ == "__main__":
    main()
