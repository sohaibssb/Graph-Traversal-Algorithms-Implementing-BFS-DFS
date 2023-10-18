import networkx as nx
import matplotlib.pyplot as plt
import time

def bfs_with_animation(graph, start_node):
    visited = set()
    queue = [start_node]
    visiting_sequence = []
    complete_sequence = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            visiting_sequence.append(node)
            neighbors = list(graph.neighbors(node))
            queue.extend(neighbors)
            complete_sequence.append(node)

            print("Visiting Sequence:", visiting_sequence)
            print("Complete Sequence:", complete_sequence)

            draw_graph_with_status(graph, visiting_sequence, complete_sequence)
            time.sleep(1) 

    return visiting_sequence, complete_sequence

def draw_graph_with_status(graph, visiting_sequence, complete_sequence):
    plt.clf()
    pos = nx.spring_layout(graph, seed=42)

    nx.draw(graph, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_color='black', font_weight='bold')

    nx.draw_networkx_nodes(graph, pos, nodelist=visiting_sequence, node_color='lightgreen', node_size=500)
    nx.draw_networkx_nodes(graph, pos, nodelist=complete_sequence, node_color='lightcoral', node_size=500)

    nx.draw_networkx_edges(graph, pos)

    plt.title("BFS Progress")
    plt.pause(0.1)
    plt.show(block=False)

#/////////  
# TASK
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])
#/////////
start_node = 1
visiting_sequence, complete_sequence = bfs_with_animation(G, start_node)
draw_graph_with_status(G, visiting_sequence, complete_sequence)
plt.show()

print("\nBFS:", complete_sequence)