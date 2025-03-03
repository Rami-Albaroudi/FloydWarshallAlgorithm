# README

## Floyd-Warshall Algorithm

This repository contains two versions of the Floyd-Warshall algorithm for finding the shortest paths between all pairs of nodes in a graph. The repository includes both **iterative** and **recursive** functions, along with sample graphs for testing, unit tests, and performance tests.

#### What is the Floyd-Warshall Algorithm?

The Floyd-Warshall algorithm is a dynamic programming approach for finding the shortest paths between all pairs of nodes in a weighted graph (binti Anuar and Said, 2016). It efficiently computes the shortest distances between every pair of nodes (binti Anuar and Said, 2016).

**Key Characteristics (binti Anuar and Said, 2016):**

- Works with both positive and negative edge weights as long as there are no negative cycles.
- Has a time complexity of O(n³) and a space complexity of O(n²) where n is the number of nodes.
- Uses a simple approach of considering each node as a potential intermediate point on a path.

**References:**

- binti Anuar, A. H. and Said, M. F. M. (2016) 'Floyd’s shortest-path algorithm theory', _Journal of Advanced Computing Research_, Vol 1(1), pp. 20-21.

---

### What is this repository for?

- **Purpose**: To provide simple implementations of the Floyd-Warshall algorithm using both recursion and iteration, test both implementations, and compare their performance.
- **Version**: 1.01
- **Key Features**:
  - Recursive and iterative implementations of Floyd-Warshall.
  - Sample graphs for testing various scenarios (ex: disconnected graphs, negative weights).
  - Unit tests to verify the algorithms' correctness.
  - Performance tests to measure the algorithms' execution items.

---

### How do I get set up?

#### 1. Clone the Repository

```
git clone <repository-url>
cd <repository-folder>
```

#### 2. Set Up the Environment

If you're using **Anaconda/Miniconda**, create and activate a virtual environment:

```
conda create --name environment_name python=3.9 -y
conda activate environment_name
```

You can also use **venv**:

```
python -m venv env
source env/bin/activate    # On macOS/Linux
env\Scripts\activate       # On Windows
```

#### 3. Install Dependencies

Install the required Python packages from `requirements.txt` by running:

```
pip install -r requirements.txt
```

---

### Running the Scripts

Both versions of the algorithm use the following sample graph:

```python
NO_PATH = maxsize # from sys import maxsize
GRAPH = [
    [0,      7,      NO_PATH, 8     ],
    [NO_PATH, 0,      5,      NO_PATH],
    [NO_PATH, NO_PATH, 0,      2     ],
    [NO_PATH, NO_PATH, NO_PATH, 0     ]
]
```

If you wish to run the algorithms using a different graph, overwrite the `GRAPH` variable in the `recursive_floyd.py` or `iterative_floyd.py` files. Please ensure you set infinite values to `NO_PATH`.

#### 1. Run the Recursive Algorithm:

```
python src/recursion/recursive_floyd.py
```

#### 2. Run the Iterative Algorithm:

```
python src/iterative/iterative_floyd.py
```

#### 3. Run Performance Tests:

The performance test compares recursive and iterative execution times across various sample graphs.

```
python src/tests/performance_test.py
```

#### 4. Run Unit Tests:

The unit tests ensure that both versions of the algorithm meet the following criteria:

- When given test input graphs, both the recursive and iterative functions' outputs match the corresponding expected output graphs.
- The recursive and iterative functions produce identical output graphs for a given input graph.

```
python src/tests/unittests.py
```

Sample input graphs and their expected outputs are outlined below.

---

### Sample Graphs

This project includes several sample graphs for testing different scenarios, including:

1. **Graph *n* Nodes**: Graphs with 2, 4, 8, and 16 nodes.
2. **Disconnected Graph**: A graph where no nodes are connected.
3. **Connected Graph**: A graph where all nodes are connected.
4. **Graph with Negative Weights**: A graph with negative weights but no negative cycles.

All sample graphs are defined in `src/tests/testgraphs.py`.

---

### Requirements

The project requires Python 3.9+ and the required packages listed in `requirements.txt`. To install all packages, run:

```
pip install -r requirements.txt
```

---

### Repository Structure

The repository is organised as follows:

```
FloydWarshallAlgorithm/
├── src/
│   ├── iterative/
│   │   ├── __init__.py             # init file for module imports.
│   │   └── iterative_floyd.py      # Iterative implementation of Floyd-Warshall.
│   ├── recursion/
│   │   ├── __init__.py             # init file for module imports.
│   │   └── recursive_floyd.py      # Recursive implementation of Floyd-Warshall.
│   └── tests/
│       ├── __init__.py             # init file for module imports.
│       ├── performance_test.py     # Performance testing script.
│       ├── testgraphs.py           # Sample graphs for testing.
│       └── unittests.py            # Unit tests.
├── LICENCE                         # Project licence.
├── README.md                       # Project documentation.
└── requirements.txt                # Required Python dependencies.
```

---

### Known Issues/Limitations

- The recursive function may be slower or return errors for larger graphs due to recursion overhead in Python.
- Both functions may produce incorrect results or return errors for graphs with negative weight cycles, since the Floyd-Warshall algorithm is not designed to handle such cases.

---

### Who do I talk to?

For questions or issues, please contact:

- **Author**: Rami Albaroudi
- **Email**: sgralbar@liverpool.ac.uk
