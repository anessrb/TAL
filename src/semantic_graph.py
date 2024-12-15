import networkx as nx


class SemanticGraph:
    def __init__(self):
        self.network = nx.DiGraph()

    def add_node(self, node, **attrs):
        self.network.add_node(node, **attrs)

    def add_edge(self, node1, node2, **attrs):
        self.network.add_edge(node1, node2, **attrs)

    def update_node(self, node, **attrs):
        """Mettre à jour les attributs d'un nœud."""
        if node in self.network.nodes:
            self.network.nodes[node].update(attrs)
        else:
            print(f"Erreur : le nœud '{node}' n'existe pas dans le graphe.")

    def visualize(self):
        import matplotlib.pyplot as plt
        pos = nx.spring_layout(self.network)
        plt.figure(figsize=(10, 8))
        nx.draw(self.network, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10)
        edge_labels = nx.get_edge_attributes(self.network, "rel_type")
        nx.draw_networkx_edge_labels(self.network, pos, edge_labels=edge_labels)
        plt.show()

    def export_to_brat(self, output_file):
        """Exporter le graphe au format BRAT."""
        with open(output_file, "w", encoding="utf-8") as f:
            entity_id = 1
            relation_id = 1

            # Export des nœuds
            for node, data in self.network.nodes(data=True):
                f.write(f"T{entity_id}\t{data.get('type', 'other')} 0 0\t{node}\n")
                entity_id += 1

            # Export des relations
            for u, v, data in self.network.edges(data=True):
                relation_type = data.get("rel_type", "r_unknown")
                f.write(f"R{relation_id}\t{relation_type} Arg1:T{u} Arg2:T{v}\n")
                relation_id += 1

        print(f"Graphe exporté au format BRAT dans : {output_file}")
