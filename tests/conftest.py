"""Test fixtures."""
import networkx as nx
import pytest


@pytest.fixture
def product_state_graph(scope="session"):
    """Graphs from Figure-1 in arXiv:1302.1604."""
    num_states = 7
    G1 = nx.Graph()
    G1.add_nodes_from(range(num_states))
    G1.add_edges_from([(0, 6), (0, 5), (0, 4), (0, 3), (1, 6), (1, 5), (1, 4), (1, 3), (2, 6), (2, 5), (2, 4), (2, 3)])

    G2 = nx.Graph()
    G2.add_nodes_from(range(num_states))
    G2.add_edges_from([(0, 1), (1, 2), (3, 6), (6, 4), (3, 5), (4, 5)])

    G3 = nx.Graph()
    G3.add_nodes_from(range(num_states))
    G3.add_edges_from([(1, 3), (2, 0), (3, 4), (5, 6)])
    return [G1, G2, G3]


@pytest.fixture
def non_product_state_graph(scope="session"):
    """Graphs from Figure-1 of arXiv:1401.7920."""
    num_states = 7
    G1 = nx.Graph()
    G1.add_nodes_from(range(num_states))
    G1.add_edges_from([(0, 1), (0, 6), (2, 4), (5, 3)])

    G2 = nx.Graph()
    G2.add_nodes_from(range(num_states))
    G2.add_edges_from([(0, 2), (0, 3), (0, 4), (0, 5), (1, 6)])

    G3 = nx.Graph()
    G3.add_nodes_from(range(num_states))
    G3.add_edges_from([(0, 3), (0, 4), (1, 3), (1, 4), (6, 3), (6, 4), (2, 5)])
    return [G1, G2, G3]