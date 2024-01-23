#Поиск от цели в глубину - DFS на графе И/ИЛИ
from LogicalNetwork import LogicalNetwork


class DFS:
    @staticmethod
    def search_from_target(logical_network, target_node, initial_set):
        executed_nodes = list() #отслеживать узлы, которые были выполнены в процессе поиска
        executed_edges = set() #keep track of edges (rule sources) that have been executed
        executed_nodes.extend(initial_set)
        printed_checked = set() #отслеживать источники правил, которые были распечатаны в процессе поиска, чтобы избежать многократной печати одного и того же источника правил

        def dfs(node): #проверяет, был ли узел посещен или нет
            if node in executed_nodes:
                return True

            #Этот блок перебирает ребра правил в логической сети. Если цель правила соответствует текущему узлу и источник не находится в выполненных ребрах, оно печатает информацию о правиле. Затем он рекурсивно вызывает функцию dfs для каждого подключенного узла правила

            for _, rule_edges in logical_network.graph.items():
                for rule_edge in rule_edges:
                    if rule_edge.rule_target == node and rule_edge.rule_source not in executed_edges:
                        if rule_edge.rule_source not in printed_checked:
                            printed_checked.add(rule_edge.rule_source)
                            print(f"{rule_edge.rule_connected_nodes} ----> {rule_edge.rule_source} ----> {rule_edge.rule_target}")

                        #This is a generator expression that applies the dfs function to each child node in rule_edge.rule_connected_nodes. It returns an iterable of the results of the dfs function for each child
                        if all(dfs(child) for child in rule_edge.rule_connected_nodes):
                            executed_nodes.append(node) #visited-посетил
                            executed_edges.add(rule_edge.rule_source)
                            return True #Значение true, чтобы указать, что целевой узел доступен из текущего узла

            return False  #Если узел не найден

        result = dfs(target_node)

        if result:
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

    print("\n Поиск от цели в глубину - DFS\n")

    #Начальный набор и Цель
    target_node_id = 14
    initial_set = [1,2,5,6,10,12,13]

    DFS.search_from_target(logical_network, target_node_id, initial_set)
