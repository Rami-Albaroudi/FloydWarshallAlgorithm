'''
File containing sample graphs for testing.
'''

from sys import maxsize
NO_PATH = maxsize

# 1. Small graph (4 nodes)
GRAPH_SMALL = [
    [0, 5, 9, 2],
    [5, 0, 3, NO_PATH],
    [9, 3, 0, 7],
    [2, NO_PATH, 7, 0]
]

# 2. Medium graph (6 nodes)
GRAPH_MEDIUM = [
    [0, 3, NO_PATH, NO_PATH, 8, 2],
    [3, 0, 1, NO_PATH, NO_PATH, NO_PATH],
    [NO_PATH, 1, 0, 2, NO_PATH, NO_PATH],
    [NO_PATH, NO_PATH, 2, 0, 4, 6],
    [8, NO_PATH, NO_PATH, 4, 0, NO_PATH],
    [2, NO_PATH, NO_PATH, 6, NO_PATH, 0]
]

# 3. Large graph (8 nodes)
GRAPH_LARGE = [
    [0, 4, NO_PATH, NO_PATH, 8, NO_PATH, NO_PATH, NO_PATH],
    [4, 0, 3, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 7],
    [NO_PATH, 3, 0, 2, NO_PATH, NO_PATH, NO_PATH, NO_PATH],
    [NO_PATH, NO_PATH, 2, 0, 5, 1, NO_PATH, NO_PATH],
    [8, NO_PATH, NO_PATH, 5, 0, NO_PATH, 9, NO_PATH],
    [NO_PATH, NO_PATH, NO_PATH, 1, NO_PATH, 0, 6, NO_PATH],
    [NO_PATH, NO_PATH, NO_PATH, NO_PATH, 9, 6, 0, 3],
    [NO_PATH, 7, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 3, 0]
]

# 4. Linear graph (path graph)
GRAPH_LINEAR = [
    [0, 1, NO_PATH, NO_PATH, NO_PATH],
    [1, 0, 2, NO_PATH, NO_PATH],
    [NO_PATH, 2, 0, 3, NO_PATH],
    [NO_PATH, NO_PATH, 3, 0, 4],
    [NO_PATH, NO_PATH, NO_PATH, 4, 0]
]

# 5. Circular graph (cycle graph)
GRAPH_CIRCULAR = [
    [0, 1, NO_PATH, NO_PATH, 5],
    [1, 0, 2, NO_PATH, NO_PATH],
    [NO_PATH, 2, 0, 3, NO_PATH],
    [NO_PATH, NO_PATH, 3, 0, 4],
    [5, NO_PATH, NO_PATH, 4, 0]
]

# 6. Complete graph (all nodes connected)
GRAPH_COMPLETE = [
    [0, 1, 2, 3, 4],
    [1, 0, 5, 6, 7],
    [2, 5, 0, 8, 9],
    [3, 6, 8, 0, 10],
    [4, 7, 9, 10, 0]
]

# 7. Incomplete graph (no path between some nodes)
GRAPH_DISCONNECTED = [
    [0, 1, 2, NO_PATH, NO_PATH, NO_PATH],
    [1, 0, 3, NO_PATH, NO_PATH, NO_PATH],
    [2, 3, 0, NO_PATH, NO_PATH, NO_PATH],
    [NO_PATH, NO_PATH, NO_PATH, 0, 4, 5],
    [NO_PATH, NO_PATH, NO_PATH, 4, 0, 6],
    [NO_PATH, NO_PATH, NO_PATH, 5, 6, 0]
]

# Dictionary of all test graphs
TEST_GRAPHS = {
    "Small": GRAPH_SMALL,
    "Medium": GRAPH_MEDIUM,
    "Large": GRAPH_LARGE,
    "Linear": GRAPH_LINEAR,
    "Circular": GRAPH_CIRCULAR,
    "Complete": GRAPH_COMPLETE,
    "Disconnected": GRAPH_DISCONNECTED,
}
