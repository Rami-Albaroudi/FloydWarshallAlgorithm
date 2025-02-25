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

    recursive_floyd(0, 0, 0)
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


def recursive_floyd(outer_loop: int, middle_loop: int, inner_loop: int):
    """
    This function computes shortest path between each pair node
    It computes by comparing a direct path with paths that have 
    intermediate nodes in the path.

    The recursive path is the shortest path function which
    calls itself to find the shortest path between a pair of nodes

    You need to increment each variable until it reaches a loop

    param: outer_loop: This variable is from the first loop of the iterative version.
    It represents the intermediate node.
    param: middle_loop: This variable is from the second loop of the iterative version
    It represents the source node.
    param: inner_loop: This variable is from the last loop of the iterative version
    It represents the destination node.
    """
    # This is the base case after we process all the paths
    if outer_loop >= MAX_LENGTH:
        return

    # Process the current node combination
    if middle_loop == inner_loop:
        GRAPH[middle_loop][inner_loop] = 0
    else:
        # Update the distance if the path through the intermediate node (outer_loop) is shorter
        GRAPH[middle_loop][inner_loop] = min(
            GRAPH[middle_loop][inner_loop],  # Current direct path
            GRAPH[middle_loop][outer_loop] +
            GRAPH[outer_loop][inner_loop]  # Path via intermediate node
        )

    # Recursive calls to handle different cases
    # Move to next inner_loop (destination node)
    if inner_loop < MAX_LENGTH - 1:
        recursive_floyd(outer_loop, middle_loop, inner_loop + 1)
    # Move to next middle_loop (source node), reset inner_loop
    elif middle_loop < MAX_LENGTH - 1:
        recursive_floyd(outer_loop, middle_loop + 1, 0)
    # Move to next outer_loop (intermediate node), reset middle_loop and inner_loop
    else:
        recursive_floyd(outer_loop + 1, 0, 0)


if __name__ == "__main__":
    main()
