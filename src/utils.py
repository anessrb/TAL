import json

def export_to_brat(graph, filename):
    with open(filename, "w") as f:
        for edge in graph.edges:
            f.write(f"{edge['src']} -> {edge['dst']} [relation={edge['relation']}, weight={edge['weight']}]\n")

def load_cache(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_cache(cache, filename):
    with open(filename, "w") as f:
        json.dump(cache, f)
