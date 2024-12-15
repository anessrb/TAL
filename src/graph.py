class Graph:
    def __init__(self):
        self.nodes = set()  # Utilisez un ensemble pour éviter les doublons
        self.edges = []  # Liste des relations

    def add_node(self, node, data=None):
        self.nodes.add(node)  # Ajout du nœud unique

    def add_edge(self, src, dst, relation, weight=1):
        # Vérifiez que src et dst existent dans les nœuds
        if src in self.nodes and dst in self.nodes:
            self.edges.append({
                "src": src,
                "dst": dst,
                "relation": relation,
                "weight": weight
            })
        else:
            print(f"Impossible d'ajouter l'arc : {src} -> {dst}, nœuds manquants.")
