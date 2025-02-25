'''
File containing a variety of sample graphs for testing.
This file can be imported into the unit testing and 
performance testing modules. 
'''

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
    [0, 3, NO_PATH, NO_PATH, 7, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 2],
    [3, 0, 1, NO_PATH, NO_PATH, 4, NO_PATH, NO_PATH, NO_PATH, NO_PATH],
    [NO_PATH, 1, 0, 6, NO_PATH, NO_PATH, 5, NO_PATH, NO_PATH, NO_PATH],
    [NO_PATH, NO_PATH, 6, 0, 2, NO_PATH, NO_PATH, 8, NO_PATH, NO_PATH],
    [7, NO_PATH, NO_PATH, 2, 0, 3, NO_PATH, NO_PATH, 4, NO_PATH],
    [NO_PATH, 4, NO_PATH, NO_PATH, 3, 0, 1, NO_PATH, NO_PATH, 6],
    [NO_PATH, NO_PATH, 5, NO_PATH, NO_PATH, 1, 0, 2.5 ,NO_PATH, 7]
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
    [NO_PATH, NO_PATH, NO_PATH, NO_PATH],
    [NO_PATH, NO_PATH, NO_PATH, NO_PATH],
    [NO_PATH, NO_PATH, NO_PATH, NO_PATH],
    [NO_PATH, NO_PATH, NO_PATH, NO_PATH]
]

# Graph with negative weights (no negative cycles)
GRAPH_NEGATIVE = [
    [0, -2, NO_PATH, NO_PATH],
    [NO_PATH, 0, -1, NO_PATH],
    [-3, NO_PATH, 0, 2],
    [NO_PATH, 1, NO_PATH, 0]
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

"""Expected outputs for each graph"""

# 2-Node Graph Expected Output
EXPECTED_GRAPH_2 = [

]

# 4-Node Graph Expected Output
EXPECTED_GRAPH_4 = [

]

# 8-Node Graph Expected Output
EXPECTED_GRAPH_8 = [

]

# 16-Node Graph Expected Output
EXPECTED_GRAPH_16 = [

]

# Connected Graph Expected Output
EXPECTED_GRAPH_CONNECTED = [

]
# Disconnected Graph Expected Output
EXPECTED_GRAPH_DISCONNECTED = [

]

# Negative Weight Graph Expected Output
EXPECTED_GRAPH_NEGATIVE = [

]

# Dictionary of all test graphs' expected results
TEST_GRAPHS_EXPECTED = {
    "2 Node Graph": EXPECTED_GRAPH_2,
    "4 Node Graph": EXPECTED_GRAPH_4,
    "8 Node Graph": EXPECTED_GRAPH_8,
    "16 Node Graph": EXPECTED_GRAPH_16,
    "Connected Graph": EXPECTED_GRAPH_CONNECTED,
    "Disconnected Graph": EXPECTED_GRAPH_DISCONNECTED,
    "Negative Weights Graph": EXPECTED_GRAPH_NEGATIVE,
}