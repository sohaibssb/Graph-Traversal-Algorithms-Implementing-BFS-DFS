#представляют структуру правила в логической сети

class RuleStructure:
    def __init__(self, source, connected_nodes, target):
        self.rule_connected_nodes = connected_nodes
        self.rule_source = source
        self.rule_target = target




