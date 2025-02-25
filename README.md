# Floyd-Warshall Algorithm #

This repository contains implementations of the Floyd-Warshall algorithm for finding the shortest paths between all pairs of nodes in a graph. The repository includes both **iterative** and **recursive** implementations, along with sample graphs for testing and performance benchmarking.

---

### What is this repository for? ###
- **Purpose**: To provide a simple and comprehensive implementation of the Floyd-Warshall algorithm using both recursion and iteration, then compare each approach's performance.
- **Version**: 1.0
- **Key Features**:
  - Recursive and iterative implementations of Floyd-Warshall.
  - Sample graphs for testing various scenarios (ex: disconnected graphs, negative weights).
  - Unit tests to verify correctness.
  - Performance benchmarking scripts.

---

### How do I get set up? ###

#### 1. Clone the Repository
```
git clone <repository-url>
cd <repository-folder>
```

#### 2. Set Up the Environment
If you're using **Anaconda**, create and activate a virtual environment:
```
conda create --name floyd_env python=3.9 -y
conda activate floyd_env
```

Alternatively, use `venv`:
```
python -m venv env
source env/bin/activate    On macOS/Linux
env\Scripts\activate       On Windows
```

#### 3. Install Dependencies
Install the required Python packages from `requirements.txt`:
```
pip install -r src/requirements.txt
```

---

### Running the Scripts ###

#### 1. Run the Recursive Implementation:
```
python src/recursion/recursive_floyd.py
```

#### 2. Run the Iterative Implementation:
```
python src/iterative/iterative_floyd.py
```

#### 3. Run Performance Tests:
The performance test compares recursive and iterative implementations across various sample graphs.
```
python src/tests/performance_test.py
```

#### 4. Run Unit Tests:
Unit tests ensure that both algorithm implementations produce correct results.
```
python -m unittest discover src/tests/
```

---

### Requirements ###

The project requires the following dependencies:
- Python 3.9 or later
- Required packages (listed in `requirements.txt`)

To install all dependencies:
```
pip install -r src/requirements.txt
```

---

### Project Structure ###

The repository is organized as follows:

```
FloydWarshallAlgorithm/
├── src/
│   ├── iterative/
│   │   ├── __init__.py             init file for module imports.
│   │   └── iterative_floyd.py      Iterative implementation of Floyd-Warshall.
│   ├── recursion/
│   │   ├── __init__.py             init file for module imports.
│   │   └── recursive_floyd.py      Recursive implementation of Floyd-Warshall.
│   ├── tests/
│   │   ├── __init__.py             init file for module imports.
│   │   ├── performance_test.py     Performance testing script.
│   │   ├── testgraphs.py           Sample graphs for testing.
│   │   └── unittests.py            Unit tests.
│   └── __init__.py                 init file for module imports.
│   └── requirements.txt            Python dependencies.
├── LICENSE                         Project license.
└── README.md                       Project documentation.
```

---

### Sample Graphs ###

This project includes several sample graphs for testing different scenarios, including:

1. **Graph n Nodes**: Graphs with between 2 to 10 nodes.
2. **Disconnected Graph**: A graph where no nodes are connected.
3. **Connected Graph**: A graph where all nodes are connected.
4. **Graph with Negative Weights**: A graph with negative weights but no negative cycles.

All sample graphs are defined in `src/tests/testgraphs.py`.

---

### Known Issues ###

- The recursive implementation may be slower for larger graphs due to recursion overhead in Python.
- The algorithm does not handle negative weight cycles since such cases may produce incorrect results.

---

### Who do I talk to? ###

For questions or issues, please contact:

- **Author**: Rami Albaroudi
- **Email**: sgralbar@liverpool.ac.uk


