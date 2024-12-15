class RuleEngine:
    def __init__(self, graph):
        self.graph = graph

    def apply_rules(self, rules):
        modified = True
        while modified:
            modified = False
            for rule in rules:
                if rule(self.graph):
                    modified = True

def rule_agent_relation(graph):
    # Exemple de règle : $x r_succ $y → $x r_agent-1 $y & $y r_agent $x
    modified = False
    for source, dest, data in list(graph.edges(data=True)):
        if data["type"] == "r_succ":
            graph.add_edge(source, dest, "r_agent-1", weight=1)
            graph.add_edge(dest, source, "r_agent", weight=1)
            modified = True
    return modified
