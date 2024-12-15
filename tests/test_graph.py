import unittest
from src.graph import Graph

class TestGraph(unittest.TestCase):
    def test_add_node(self):
        graph = Graph()
        graph.add_node("chat")
        self.assertIn("chat", graph.nodes)

    def test_add_edge(self):
        graph = Graph()
        graph.add_node("chat")
        graph.add_node("boit")
        graph.add_edge("chat", "boit", "r_action")
        self.assertEqual(len(graph.edges), 1)
