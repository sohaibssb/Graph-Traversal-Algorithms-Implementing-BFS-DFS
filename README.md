# Graph Traversal Algorithms: Implementing BFS & DFS
Implement Breadth-First Search & Depth-First Search Algorithms

Programmed by Sohaibssb as a part of Expert systems design Course at Bauman University, Moscow. 2023.

------------------

Lab1-BFS:
Breadth-First Search is an algorithm for traversing or searching tree or graph data structures. It starts at the root node (or any arbitrary node) and explores all neighbor nodes at the present depth before moving to nodes at the next depth level. BFS uses a queue data structure to keep track of the nodes to be visited. It is often used to find the shortest path in unweighted graphs, explore all possible paths in a tree, and can be useful for algorithms like shortest path algorithms and network analysis.

Benefits of BFS:

        Finds the shortest path in an unweighted graph.
        Can be used for web crawling and social network analysis.
        Guarantees the shortest path when used for pathfinding.
        Can be used for network troubleshooting, such as finding the shortest path in computer networks.

Lab1-DFS:
Depth-First Search is another algorithm for traversing or searching tree or graph data structures. In DFS, the algorithm starts at the root node (or any arbitrary node) and explores as far as possible along each branch before backtracking. It uses a stack or recursion to keep track of nodes to be visited. DFS is commonly used in problems involving cycle detection, topological sorting, and solving puzzles, among other applications.

Benefits of DFS:

        Requires less memory compared to BFS, making it suitable for deep graphs.
        Useful in problems involving cycle detection, e.g., in compilers for syntax analysis.
        Applicable for topological sorting, where tasks must be executed in a specific order.
        Often used in solving puzzles and games, such as chess and mazes.

Lab2-Breadth-first search (reverse) - BFS on AND/OR graph

Lab3-Depth-first search - DFS on AND/OR graph

------------------

Libraries and tchnologies used in this program:

    NetworkX: NetworkX is a Python library used for creating, manipulating, and studying the structure, dynamics, and functions of complex networks (e.g., graphs).

    Matplotlib: Matplotlib is a widely-used Python library for creating static, animated, and interactive visualizations in Python.

    Time: The time module is a Python standard library module used to introduce delays in the code for animation purposes. It is used to slow down the visualization to observe the step-by-step execution.
