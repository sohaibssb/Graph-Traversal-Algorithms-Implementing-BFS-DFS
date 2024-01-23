#Поиск от цели (обратный )  в ширину - BFS на графе И/ИЛИ
from LogicalNetwork import LogicalNetwork

class BFS:
    @staticmethod
    def search_from_initial_nodes(logical_network, target_node, initial_set):
        executed_edges = set()

        def bfs(current_executed_nodes, path):
            if target_node in current_executed_nodes:
                return True, set(current_executed_nodes), path

            for node in current_executed_nodes:
                for rule_edge in logical_network.graph.get(node, []):#извлекает список ребер правила, связанных с определенным узлом. Если у узла нет правил, он возвращает пустой список


                    if rule_edge.rule_source not in executed_edges and set(rule_edge.rule_connected_nodes).issubset(current_executed_nodes):

                    #if set(rule_edge.rule_connected_nodes).issubset(current_executed_nodes): #При этом проверяется, входят ли все подключенные узлы ребра правила в текущий набор исполняемых узлов.
                        print(f"{rule_edge.rule_connected_nodes} ----> {rule_edge.rule_source} ----> {rule_edge.rule_target}")
                        executed_edges.add(rule_edge.rule_source)

                        result, new_nodes, new_path = bfs(
                            current_executed_nodes + [rule_edge.rule_target], path + [rule_edge.rule_source]
                        ) #Функция BFS рекурсивно вызывается с обновленным набором исполняемых узлов и пути

                        if result:
                            return True, new_nodes, new_path

            return False, set(current_executed_nodes), path #Верните False, если цель не найдена

        #found = bfs(initial_set, [])
        found, closed_nodes, closed_edges = bfs(initial_set, [])
        
        #Closed_nodes — это набор, содержащий все узлы, посещенные во время обхода BFS
        #closed_edges is a set containing all the edges visited during the BFS traversal

        #проверяет, находится ли целевой_узел в наборе закрытых_узлов. Если целевой узел находится в наборе, это означает, что цель достижима из исходного набора узлов. Если целевой узел отсутствует в наборе, это означает, что цель недоступна


        if found and target_node in closed_nodes:
            print("\n")
            print(f"Target Node: {target_node}")
            print(f"Initial Nodes: {initial_set}")
            print("Results: Target Reachable - Достижима\n")
        else:
            print("\n")
            print(f"Target Node: {target_node}")
            print(f"Initial Nodes: {initial_set}")
            print("Results: Target Unreachable - Недостижима\n")

if __name__ == "__main__":
    rules = [
        {"source": 104, "connected_nodes": [8, 31], "target": 3},
        {"source": 101, "connected_nodes": [1, 2], "target": 3},
        {"source": 103, "connected_nodes": [5, 6], "target": 4},
        {"source": 102, "connected_nodes": [3, 2, 4], "target": 7},
        {"source": 107, "connected_nodes": [12, 13], "target": 11},
        {"source": 106, "connected_nodes": [4, 10, 11], "target": 9},
        {"source": 111, "connected_nodes": [18, 32], "target": 9},
        {"source": 105, "connected_nodes": [7, 9], "target": 14},
        {"source": 112, "connected_nodes": [19, 20], "target": 34},
        {"source": 109, "connected_nodes": [16, 17], "target": 15},
        {"source": 108, "connected_nodes": [34, 15], "target": 33},
        {"source": 110, "connected_nodes": [9, 34], "target": 14},
    ]

    logical_network = LogicalNetwork()

    for rule in rules:
        logical_network.add_rule_edge(rule["source"], rule["connected_nodes"], rule["target"])

    logical_network.display_logical_network()

    print("\n Поиск от цели (обратный )  в ширину - BFS\n")

    #Начальный набор и Цель
    initial_set = [1,2,5,6,10,12,13]
    target_node_id = 14

    BFS.search_from_initial_nodes(logical_network, target_node_id, initial_set)
