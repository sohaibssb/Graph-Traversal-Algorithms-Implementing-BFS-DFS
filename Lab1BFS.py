import networkx as nx
import matplotlib.pyplot as plt

def bfs(graph, start_node):
    visited = set()
    queue = [start_node]
    bfs_tree = nx.Graph()

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            neighbors = list(graph.neighbors(node))
            queue.extend(neighbors)
            bfs_tree.add_edges_from((node, neighbor) for neighbor in neighbors if neighbor not in bfs_tree.nodes)

    return bfs_tree

# Create a sample graph (you can modify this to your own graph)
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])

# Specify the starting node for BFS
start_node = 1

# Run BFS and obtain the BFS tree
bfs_tree = bfs(G, start_node)

# Plot the original graph and BFS tree
plt.figure(figsize=(12, 6))

# Original Graph
plt.subplot(121)
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_color='black', font_weight='bold')
plt.title("Original Graph")

# BFS Tree
plt.subplot(122)
pos = nx.spring_layout(bfs_tree, seed=42)
nx.draw(bfs_tree, pos, with_labels=True, node_size=500, node_color='lightgreen', font_size=12, font_color='black', font_weight='bold')
plt.title("BFS Tree")

plt.tight_layout()
plt.show()
