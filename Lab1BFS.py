import networkx as nx
import matplotlib.pyplot as plt
import time


#начало алгоритма работы функции
#/////////////////////////////////////////////////////////////
def bfs_with_animation(graph, start_node):
    visited = set() #Посещенный набор
    queue = [start_node] #Начальный узел
    visiting_sequence = [] #последовательность посещений
    complete_sequence = [] #полная последовательность

    while queue:
        node = queue.pop(0) # Вывести из очереди первый узел в очереди
        if node not in visited:  # Проверьте, не был ли посещен узел
            # Пометить узел как посещенный
            visited.add(node)
            # Запишите узел как посещенный
            visiting_sequence.append(node)
            # Найти соседей текущего узла
            neighbors = list(graph.neighbors(node))
            # Поставьте соседей в очередь для изучения в следующем раунде
            queue.extend(neighbors)
            # Запишите узел как завершенный
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
start_node = 7
visiting_sequence, complete_sequence = bfs_with_animation(G, start_node)
draw_graph_with_status(G, visiting_sequence, complete_sequence)
plt.show()

print("\nBFS:", complete_sequence)