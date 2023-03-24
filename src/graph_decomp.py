"""https://sun.iwu.edu/~mliffito/publications/ictai17_zhao_graph_decomp.pdf"""
import networkx as nx
from pysat.formula import CNF

def encode(G, H):
    # For a graph decomposition, the number of copies (blocks) is given by:
    copies = G.number_of_edges() // H.number_of_edges()

    # For each copy of H, associate one copy of G 
    for i in range(copies):
        for j in range(G.number_of_nodes):
            pass


G1_1 = nx.complete_bipartite_graph(2, 1)
G1_2 = nx.complete_bipartite_graph(2, 1)
G1_3 = nx.complete_bipartite_graph(1, 1)

G2_1 = nx.complete_bipartite_graph(4, 1)
G2_2 = nx.complete_bipartite_graph(1, 1)

G3_1 = nx.complete_bipartite_graph(3, 2)
G3_2 = nx.complete_bipartite_graph(1, 1)

G1 = nx.disjoint_union(G1_1, G1_2)
G2 = nx.disjoint_union(G2_1, G2_2)
G3 = nx.disjoint_union(G3_1, G3_2)

encode(G1, G2)

import networkx as nx

def is_edge_coloring_of_complete_graph(G):
    """Checks whether an orthogonality graph is an edge coloring of the complete graph."""
    
    # Check that the graph is connected and has no self-loops
    if not nx.is_connected(G) or any(G.has_edge(v, v) for v in G):
        return False
    
    # Check that every vertex corresponds to a distinct color
    colors = set(G.nodes())
    if len(colors) != len(G):
        return False
    
    # Check that every edge corresponds to a pair of vertices with non-empty intersection
    for u, v in G.edges():
        if not set(u).intersection(set(v)):
            return False
        
    # Check that every pair of edges that share a common endpoint correspond to vertices with empty intersection
    for u, v, w in nx.triangles(G):
        if set(u).intersection(set(v)) and set(u).intersection(set(w)):
            return False
        if set(v).intersection(set(u)) and set(v).intersection(set(w)):
            return False
        if set(w).intersection(set(u)) and set(w).intersection(set(v)):
            return False
    
    # If all checks pass, the graph is an edge coloring of the complete graph
    return True

G1_1 = nx.complete_bipartite_graph(3, 2)
G1_2 = nx.complete_bipartite_graph(1, 1)
G1 = nx.disjoint_union(G1_1, G1_2)

print(is_edge_coloring_of_complete_graph(G1))
