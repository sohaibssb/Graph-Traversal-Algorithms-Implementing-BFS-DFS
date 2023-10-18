import networkx as nx
import matplotlib.pyplot as plt
import time

def dfs_with_animation(graph, start_node):
    visited = set()
    stack = [start_node]
    visiting_sequence = []
    complete_sequence = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            visiting_sequence.append(node)
            neighbors = list(graph.neighbors(node))
            stack.extend(neighbor for neighbor in neighbors if neighbor not in visited)
            complete_sequence.append(node)

            # Print the current visiting and complete sequences
            print("Visiting Sequence:", visiting_sequence)
            print("Complete Sequence:", complete_sequence)

            # Create a visualization for the current state of the DFS
            draw_graph_with_status(graph, visiting_sequence, complete_sequence)
            time.sleep(1)  # Adjust the delay as needed (1 second in this example)

    return visiting_sequence, complete_sequence

def draw_graph_with_status(graph, visiting_sequence, complete_sequence):
    plt.clf()
    pos = nx.spring_layout(graph, seed=42)

    # Draw nodes
    nx.draw(graph, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_color='black', font_weight='bold')

    # Highlight nodes that are currently visiting and those that have been visited
    nx.draw_networkx_nodes(graph, pos, nodelist=visiting_sequence, node_color='lightgreen', node_size=500)
    nx.draw_networkx_nodes(graph, pos, nodelist=complete_sequence, node_color='lightcoral', node_size=500)

    # Draw edges
    nx.draw_networkx_edges(graph, pos)

    plt.title("DFS Progress")
    plt.pause(0.1)
    plt.show(block=False)

# Create a sample graph (you can modify this to your own graph)
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])

# Specify the starting node for DFS
start_node = 1

# Run DFS with animation and obtain the visiting and completing sequences
visiting_sequence, complete_sequence = dfs_with_animation(G, start_node)

# Display the final state of the DFS graph
draw_graph_with_status(G, visiting_sequence, complete_sequence)
plt.show()
