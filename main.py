import networkx as nx
from src.jdm_api import JeuxDeMotsAPI
from src.semantic_graph import SemanticGraph

rules = [
    {
        "conditions": [
            {"type": "GN", "relation": "r_succ", "target_type": "GV"}
        ],
        "actions": [
            {"relation": "r_agent", "weight": 10}
        ]
    },
    {
        "conditions": [
            {"type": "GV", "relation": "r_succ", "target_type": "GN"}
        ],
        "actions": [
            {"relation": "r_patient", "weight": 10}
        ]
    }
]

def main():
    # Initialisation
    jdm_api = JeuxDeMotsAPI()
    graph = SemanticGraph()

    # Exemple de texte
    texte = "Le chien regarde le chat dans le jardin."
    print(f"Texte analysé : {texte}")

    # Tokenisation simple
    tokens = texte.split()
    print("Tokens détectés :", tokens)

    # Étape 1 : Construction du graphe initial
    build_initial_graph(graph, tokens)

    # Étape 2 : Ajout des relations morphosyntaxiques
    add_morphological_relations(graph, tokens, jdm_api)

    # Étape 3 : Ajout des relations sémantiques
    add_semantic_relations(graph)

    # Étape 4 : Application des règles
    apply_rules(graph, rules)

    # Étape 5 : Désambiguïsation
    disambiguate_graph(graph, jdm_api)

    # Étape 6 : Visualisation et exportation
    print("\n--- Résumé du Graphe ---")
    graph.visualize()
    graph.export_to_brat("data/results/output.ann")
    print("\nGraphe exporté dans : data/results/output.ann")

def build_initial_graph(graph, tokens):
    """Construire un graphe linéaire initial avec les relations r_succ."""
    graph.add_node("_START", type="start")
    graph.add_node("_END", type="end")

    for i, token in enumerate(tokens):
        graph.add_node(token, type="word")
        if i == 0:
            graph.add_edge("_START", token, rel_type="r_succ", weight=1)
        else:
            graph.add_edge(tokens[i - 1], token, rel_type="r_succ", weight=1)

    graph.add_edge(tokens[-1], "_END", rel_type="r_succ", weight=1)
    print("Relations r_succ ajoutées au graphe.")



def add_morphological_relations(graph, tokens, jdm_api):
    """Ajouter des relations morphosyntaxiques (e.g., r_pos) et attribuer des types."""
    for token in tokens:
        print(f"\nTraitement morphosyntaxique du token : {token}")
        morpho_data = jdm_api.get_morphological_data(token)

        if morpho_data and isinstance(morpho_data, list):
            for relation in morpho_data:
                if relation["type"] == "r_pos":
                    graph.add_edge(token, relation["name"], rel_type="r_pos", weight=relation["weight"])
                    print(f"Relation ajoutée : {token} -> {relation['name']} [r_pos, poids={relation['weight']}]")
        else:
            print(f"Aucune donnée morphologique trouvée pour le token : {token}")

    # Attribuer des types simples
    assign_node_types(graph, tokens)

def assign_node_types(graph, tokens):
    """Attribuer des types aux nœuds en fonction de leur rôle grammatical."""
    for token in tokens:
        if token in ["chat", "lait", "chèvre"]:
            graph.update_node(token, type="GN")
        elif token in ["boit"]:
            graph.update_node(token, type="GV")
        else:
            graph.update_node(token, type="other")



def add_semantic_relations(graph):
    """Ajouter des relations sémantiques comme r_agent et r_patient."""
    for edge in list(graph.network.edges(data=True)):
        node1, node2, data = edge
        node1_data = graph.network.nodes[node1]
        node2_data = graph.network.nodes[node2]

        # Vérification des types des nœuds et ajout des relations
        if node1_data.get("type") == "GN" and node2_data.get("type") == "GV":
            graph.add_edge(node1, node2, rel_type="r_agent", weight=10)
            print(f"Relation ajoutée : {node1} -> {node2} [r_agent, poids=10]")
        elif node1_data.get("type") == "GV" and node2_data.get("type") == "GN":
            graph.add_edge(node1, node2, rel_type="r_patient", weight=10)
            print(f"Relation ajoutée : {node1} -> {node2} [r_patient, poids=10]")


def apply_rules(graph, rules):
    """Appliquer les règles définies pour enrichir le graphe."""
    for rule in rules:
        for edge in list(graph.network.edges(data=True)):
            node1, node2, data = edge
            node1_data = graph.network.nodes[node1]
            node2_data = graph.network.nodes[node2]

            # Vérification des conditions de la règle
            if node1_data.get("type") == rule["conditions"][0]["type"] and \
               data.get("rel_type") == rule["conditions"][0]["relation"] and \
               node2_data.get("type") == rule["conditions"][0]["target_type"]:
                # Appliquer les actions
                for action in rule["actions"]:
                    graph.add_edge(node1, node2, rel_type=action["relation"], weight=action["weight"])
                    print(f"Règle appliquée : {node1} -> {node2} [{action['relation']}, poids={action['weight']}]")


def disambiguate_graph(graph, jdm_api):
    """Désambiguïser les nœuds en utilisant les relations de raffinement sémantique."""
    for node, data in list(graph.network.nodes(data=True)):
        if "ambiguity" in data:
            possible_senses = jdm_api.get_possible_senses(node)
            if possible_senses:
                best_sense = max(possible_senses, key=lambda sense: sense["weight"])
                graph.update_node(node, name=best_sense["name"], weight=best_sense["weight"])
                print(f"Désambiguïsation : {node} -> {best_sense['name']} (poids={best_sense['weight']})")

if __name__ == "__main__":
    main()
