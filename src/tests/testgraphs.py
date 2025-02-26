'''
File containing a variety of manually-created sample graphs for testing
as well as their expected outputs after being processed by the
algorithm. This file can be imported into the unit testing and 
performance testing modules. 
'''


# Imports
from sys import maxsize
NO_PATH = maxsize

# Test graphs

# 2-Node Graph
GRAPH_2 = [
    [0, 5],
    [5, 0]
]

# 4-Node Graph
GRAPH_4 = [
    [0, 5, 9, 2],
    [5, 0, 3, NO_PATH],
    [9, 3, 0, 7],
    [2, NO_PATH, 7, 0]
]

# 8-Node Graph
GRAPH_8 = [
    [0, 4, NO_PATH, NO_PATH, 8, NO_PATH, NO_PATH, NO_PATH],
    [4, 0, 3, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 7],
    [NO_PATH, 3, 0, 2, NO_PATH, NO_PATH, NO_PATH, NO_PATH],
    [NO_PATH, NO_PATH, 2, 0, 5, 1, NO_PATH, NO_PATH],
    [8, NO_PATH, NO_PATH, 5, 0, NO_PATH, 9, NO_PATH],
    [NO_PATH, NO_PATH, NO_PATH, 1, NO_PATH, 0, 6, NO_PATH],
    [NO_PATH, NO_PATH, NO_PATH, NO_PATH, 9, 6, 0, 3],
    [NO_PATH, 7, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 3, 0]
]

# 16-Node Graph
GRAPH_16 = [
    [0, 5, 7, NO_PATH, 2, NO_PATH, 9, NO_PATH, 4,
        NO_PATH, 8, NO_PATH, NO_PATH, 6, NO_PATH, 3],
    [5, 0, NO_PATH, 4, NO_PATH, 8, NO_PATH, 2, NO_PATH,
        7, NO_PATH, 9, NO_PATH, NO_PATH, 5, NO_PATH],
    [7, NO_PATH, 0, 6, NO_PATH, NO_PATH, 3, NO_PATH, NO_PATH,
        NO_PATH, 2, NO_PATH, 8, NO_PATH, NO_PATH, 4],
    [NO_PATH, 4, 6, 0, 9, NO_PATH, NO_PATH, 5, NO_PATH,
        NO_PATH, NO_PATH, 3, NO_PATH, NO_PATH, 7, NO_PATH],
    [2, NO_PATH, NO_PATH, 9, 0, 7, NO_PATH, NO_PATH, 6,
        NO_PATH, NO_PATH, NO_PATH, 4, NO_PATH, NO_PATH, 8],
    [NO_PATH, 8, NO_PATH, NO_PATH, 7, 0, 5, NO_PATH, NO_PATH,
        3, NO_PATH, NO_PATH, NO_PATH, 9, NO_PATH, NO_PATH],
    [9, NO_PATH, 3, NO_PATH, NO_PATH, 5, 0, 8, NO_PATH,
        NO_PATH, 4, NO_PATH, NO_PATH, NO_PATH, 6, NO_PATH],
    [NO_PATH, 2, NO_PATH, 5, NO_PATH, NO_PATH, 8, 0, 7,
        NO_PATH, NO_PATH, 6, NO_PATH, NO_PATH, NO_PATH, 9],
    [4, NO_PATH, NO_PATH, NO_PATH, 6, NO_PATH, NO_PATH, 7, 0,
        5, NO_PATH, NO_PATH, 3, NO_PATH, NO_PATH, NO_PATH],
    [NO_PATH, 7, NO_PATH, NO_PATH, NO_PATH, 3, NO_PATH, NO_PATH,
        5, 0, 9, NO_PATH, NO_PATH, 4, NO_PATH, NO_PATH],
    [8, NO_PATH, 2, NO_PATH, NO_PATH, NO_PATH, 4, NO_PATH,
        NO_PATH, 9, 0, 7, NO_PATH, NO_PATH, 5, NO_PATH],
    [NO_PATH, 9, NO_PATH, 3, NO_PATH, NO_PATH, NO_PATH, 6,
        NO_PATH, NO_PATH, 7, 0, 8, NO_PATH, NO_PATH, 2],
    [NO_PATH, NO_PATH, 8, NO_PATH, 4, NO_PATH, NO_PATH, NO_PATH,
        3, NO_PATH, NO_PATH, 8, 0, 6, NO_PATH, NO_PATH],
    [6, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 9, NO_PATH, NO_PATH,
        NO_PATH, 4, NO_PATH, NO_PATH, 6, 0, 3, NO_PATH],
    [NO_PATH, 5, NO_PATH, 7, NO_PATH, NO_PATH, 6, NO_PATH,
        NO_PATH, NO_PATH, 5, NO_PATH, NO_PATH, 3, 0, 8],
    [3, NO_PATH, 4, NO_PATH, 8, NO_PATH, NO_PATH, 9,
        NO_PATH, NO_PATH, NO_PATH, 2, NO_PATH, NO_PATH, 8, 0]
]

# Connected graph (all nodes connected)
GRAPH_CONNECTED = [
    [0, 1, 2, 3, 4],
    [1, 0, 5, 6, 7],
    [2, 5, 0, 8, 9],
    [3, 6, 8, 0, 10],
    [4, 7, 9, 10, 0]
]

# Disconnected graph (all nodes not connected)
GRAPH_DISCONNECTED = [
    [0, NO_PATH, NO_PATH, NO_PATH],
    [NO_PATH, 0, NO_PATH, NO_PATH],
    [NO_PATH, NO_PATH, 0, NO_PATH],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]

# Graph with negative weights (no negative cycles)
GRAPH_NEGATIVE = [
    [0, 4, 3],
    [NO_PATH, 0, -2],
    [NO_PATH, NO_PATH, 0]
]

# Expected outputs for test graphs were calculated manually using
# https://www.pisqre.com/calculator/Floyd-Warshall

# 2-Node Graph Expected Output
EXPECTED_GRAPH_2 = [
    [0, 5],
    [5, 0]
]

# 4-Node Graph Expected Output
EXPECTED_GRAPH_4 = [
    [0, 5, 8, 2],
    [5, 0, 3, 7],
    [8, 3, 0, 7],
    [2, 7, 7, 0]
]

# 8-Node Graph Expected Output
EXPECTED_GRAPH_8 = [
    [0, 4, 7, 9, 8, 10, 14, 11],
    [4, 0, 3, 5, 10, 6, 10, 7],
    [7, 3, 0, 2, 7, 3, 9, 10],
    [9, 5, 2, 0, 5, 1, 7, 10],
    [8, 10, 7, 5, 0, 6, 9, 12],
    [10, 6, 3, 1, 6, 0, 6, 9],
    [14, 10, 9, 7, 9, 6, 0, 3],
    [11, 7, 10, 10, 12, 9, 3, 0]
]

# 16-Node Graph Expected Output
EXPECTED_GRAPH_16 = [
    [0, 5, 7, 8, 2, 9, 9, 7, 4, 9, 8, 5, 6, 6, 9, 3],
    [5, 0, 10, 4, 7, 8, 10, 2, 9, 7, 10, 7, 11, 8, 5, 8],
    [7, 10, 0, 6, 9, 8, 3, 11, 11, 11, 2, 6, 8, 10, 7, 4],
    [8, 4, 6, 0, 9, 12, 9, 5, 12, 11, 8, 3, 11, 10, 7, 5],
    [2, 7, 9, 9, 0, 7, 11, 9, 6, 10, 10, 7, 4, 8, 11, 5],
    [9, 8, 8, 12, 7, 0, 5, 10, 8, 3, 9, 14, 11, 7, 10, 12],
    [9, 10, 3, 9, 11, 5, 0, 8, 13, 8, 4, 9, 11, 9, 6, 7],
    [7, 2, 11, 5, 9, 10, 8, 0, 7, 9, 12, 6, 10, 10, 7, 8],
    [4, 9, 11, 12, 6, 8, 13, 7, 0, 5, 12, 9, 3, 9, 12, 7],
    [9, 7, 11, 11, 10, 3, 8, 9, 5, 0, 9, 14, 8, 4, 7, 12],
    [8, 10, 2, 8, 10, 9, 4, 12, 12, 9, 0, 7, 10, 8, 5, 6],
    [5, 7, 6, 3, 7, 14, 9, 6, 9, 14, 7, 0, 8, 11, 10, 2],
    [6, 11, 8, 11, 4, 11, 11, 10, 3, 8, 10, 8, 0, 6, 9, 9],
    [6, 8, 10, 10, 8, 7, 9, 10, 9, 4, 8, 11, 6, 0, 3, 9],
    [9, 5, 7, 7, 11, 10, 6, 7, 12, 7, 5, 10, 9, 3, 0, 8],
    [3, 8, 4, 5, 5, 12, 7, 8, 7, 12, 6, 2, 9, 9, 8, 0]
]

# Connected Graph Expected Output
EXPECTED_GRAPH_CONNECTED = [
    [0, 1, 2, 3, 4],
    [1, 0, 3, 4, 5],
    [2, 3, 0, 5, 6],
    [3, 4, 5, 0, 7],
    [4, 5, 6, 7, 0]
]

# Disconnected Graph Expected Output
EXPECTED_GRAPH_DISCONNECTED = [
    [0, NO_PATH, NO_PATH, NO_PATH],
    [NO_PATH, 0, NO_PATH, NO_PATH],
    [NO_PATH, NO_PATH, 0, NO_PATH],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]

# Negative Weight Graph Expected Output
EXPECTED_GRAPH_NEGATIVE = [
    [0, 4, 2],
    [NO_PATH, 0, -2],
    [NO_PATH, NO_PATH, 0]
]

# Dictionary of all test graphs
TEST_GRAPHS = {
    "2 Node Graph": GRAPH_2,
    "4 Node Graph": GRAPH_4,
    "8 Node Graph": GRAPH_8,
    "16 Node Graph": GRAPH_16,
    "Connected Graph": GRAPH_CONNECTED,
    "Disconnected Graph": GRAPH_DISCONNECTED,
    "Negative Weights Graph": GRAPH_NEGATIVE,
}

# Dictionary of all test graphs' expected outputs
TEST_GRAPHS_EXPECTED = {
    "2 Node Graph": EXPECTED_GRAPH_2,
    "4 Node Graph": EXPECTED_GRAPH_4,
    "8 Node Graph": EXPECTED_GRAPH_8,
    "16 Node Graph": EXPECTED_GRAPH_16,
    "Connected Graph": EXPECTED_GRAPH_CONNECTED,
    "Disconnected Graph": EXPECTED_GRAPH_DISCONNECTED,
    "Negative Weights Graph": EXPECTED_GRAPH_NEGATIVE,
}
