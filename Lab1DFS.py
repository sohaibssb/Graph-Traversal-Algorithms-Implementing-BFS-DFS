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

            print("Visiting Sequence:", visiting_sequence)
            print("Complete Sequence:", complete_sequence)

            draw_graph_with_status(graph, visiting_sequence, complete_sequence)
            time.sleep(2) 

    return visiting_sequence, complete_sequence

def draw_graph_with_status(graph, visiting_sequence, complete_sequence):
    plt.clf()
    pos = nx.spring_layout(graph, seed=42)

    nx.draw(graph, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_color='black', font_weight='bold')

    nx.draw_networkx_nodes(graph, pos, nodelist=visiting_sequence, node_color='lightgreen', node_size=500)
    nx.draw_networkx_nodes(graph, pos, nodelist=complete_sequence, node_color='lightcoral', node_size=500)

    nx.draw_networkx_edges(graph, pos)

    plt.gca().set_title("DFS Progress")
    plt.pause(0.1)
    plt.show(block=False)

#/////////  
# TASK
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])
#/////////  
start_node = 5
visiting_sequence, complete_sequence = dfs_with_animation(G, start_node)
draw_graph_with_status(G, visiting_sequence, complete_sequence)
plt.show()

print("\nDFS:", complete_sequence)