from RuleStructure import RuleStructure

#This Class Represents a logical network based on a set of rules
#Этот класс представляет логическую сеть, основанную на наборе правил.

class LogicalNetwork:
    
    #конструктор логической сети
    def __init__(self, rule_edges=None):
        self.graph = {} #Dictionary
        if rule_edges is not None:
            self.build_logical_network(rule_edges)

    #принимает список rule_edges и заполняет словарь графов
    def build_logical_network(self, rule_edges):
        for rule_edge in rule_edges:
            for node in rule_edge.rule_connected_nodes:
                self.graph.setdefault(node, []).append(rule_edge)

    #добавляет новое правило в логическую сеть
    def add_rule_edge(self, source, connected_nodes, target):
        rule_edge = RuleStructure(source, connected_nodes, target)
        for node in connected_nodes:
            self.graph.setdefault(node, []).append(rule_edge)

    
    def display_logical_network(self):
        printed_rule_nodes = set()
        print("\nГрафе И/ИЛИ:\n")
        for node, rule_edges in self.graph.items():
            for rule_edge in rule_edges:
                if rule_edge.rule_source not in printed_rule_nodes:
                    print(f"{rule_edge.rule_connected_nodes} ----> {rule_edge.rule_source} ----> {rule_edge.rule_target}:")
                    printed_rule_nodes.add(rule_edge.rule_source)
