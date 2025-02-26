'''
File containing a variety of manually-created sample graphs for testing
as well as their expected outputs after being processed by the
algorithm. This file can be imported into the unit testing and 
performance testing modules. 
'''

''' Performance test graphs '''

# Imports
from sys import maxsize
NO_PATH = maxsize

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
    [0, -2, NO_PATH, NO_PATH],
    [NO_PATH, 0, -1, NO_PATH],
    [-3, NO_PATH, 0, 2],
    [NO_PATH, 1, NO_PATH, 0]
]

# Dictionary of all performance test graphs
PERFORMANCE_GRAPHS = {
    "2 Node Graph": GRAPH_2,
    "4 Node Graph": GRAPH_4,
    "8 Node Graph": GRAPH_8,
    "16 Node Graph": GRAPH_16,
    "Connected Graph": GRAPH_CONNECTED,
    "Disconnected Graph": GRAPH_DISCONNECTED,
    "Negative Weights Graph": GRAPH_NEGATIVE,
}

"""Unit test graphs and their expected outputs"""

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

# Connected Graph Expected Output
EXPECTED_GRAPH_CONNECTED = [
    [0, 1, 2, 3, 4],
    [1, 0, 5, 6, 7],
    [2, 5, 0, 8, 9],
    [3, 6, 8, 0, 10],
    [4, 7, 9, 10, 0]
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
    [0, -2, -3, -1],
    [1, 0, -1, 1],
    [-3, -5, 0, 2],
    [0, -2, -3, 0]
]

# Dictionary of all unit test graphs
UNITTEST_GRAPHS = {
    "2 Node Graph": GRAPH_2,
    "4 Node Graph": GRAPH_4,
    "Connected Graph": GRAPH_CONNECTED,
    "Disconnected Graph": GRAPH_DISCONNECTED,
    "Negative Weights Graph": GRAPH_NEGATIVE,
}

# Dictionary of all unit test graphs' expected outputs
UNITTEST_GRAPHS_EXPECTED = {
    "2 Node Graph": EXPECTED_GRAPH_2,
    "4 Node Graph": EXPECTED_GRAPH_4,
    "Connected Graph": EXPECTED_GRAPH_CONNECTED,
    "Disconnected Graph": EXPECTED_GRAPH_DISCONNECTED,
    "Negative Weights Graph": EXPECTED_GRAPH_NEGATIVE,
}
