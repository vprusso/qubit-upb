from dataclasses import dataclass

import itertools
import networkx as nx



@dataclass
class Node:
    neighbors: set[int]
    reachable_nodes: set[int]
    #equal_nodes: set[int] = None
    #orthogonal_nodes: set[int] = None


@dataclass
class OrthogonalityGraph:
    nodes: dict[int, Node]


def construct_graph_relations(graphs):
    orthog_graphs = []
    for graph in graphs:
        nodes = {}
        for node in graph.nodes():
            neighbors = set([n for n in graph.neighbors(node)])
            reachable_nodes = set(nx.descendants(graph, node)) - set(neighbors)
            nodes[node] = Node(neighbors, reachable_nodes)
        orthog_graphs.append(OrthogonalityGraph(nodes))
    return orthog_graphs


def is_upb(graphs):
    orthog_graphs = construct_graph_relations(graphs)

    all_relations = []
    for graph in orthog_graphs:
        nodes = graph.nodes

        relations = {}
        for node in nodes:
            neighbors = nodes[node].neighbors
            if tuple(neighbors) not in relations:
                relations[tuple(neighbors)] = [{node}]
            else:
                relations[tuple(neighbors)].append({node})

        graph_relations = []
        for k, v in relations.items():
            relations[k] = set().union(*v)
            graph_relations.append(set(k))
        all_relations.append(graph_relations)

    shaded = list(itertools.product(*all_relations))

    for s in shaded:
        if set().union(*s) == set(range(num_states)):
            return False
    return True

def is_product_basis(graphs: list[OrthogonalityGraph]) -> bool:
    """Check if set of orthogonality graphs form a product basis.

    A set of orthogonality graphs form a product basis if every edge is present
    in at least one of the graphs.
    """
    combined_graph = nx.Graph()
    for graph in graphs:
        combined_graph = nx.compose(combined_graph, graph)

    nodes = len(combined_graph.nodes)
    edges = set(combined_graph.edges)
    all_edges = {(i, j) for i in range(nodes) for j in range(i, nodes) if i != j}

    return all_edges - edges == set()

def is_extendible(graphs):
    """Check if set of orthogonality graphs are extendible.

    A set of orthogonality graphs are extendible if we can find a product state
    that is orthogonal to the all the states amongst the graphs.
    """
    pass


num_states = 7
# Graphs from Figure-1 in arXiv:1302.1604
G1 = nx.Graph()
G1.add_nodes_from(range(num_states))
G1.add_edges_from([(0, 6), (0, 5), (0, 4), (0, 3), (1, 6), (1, 5), (1, 4), (1, 3), (2, 6), (2, 5), (2, 4), (2, 3)])

G2 = nx.Graph()
G2.add_nodes_from(range(num_states))
G2.add_edges_from([(0, 1), (1, 2), (3, 6), (6, 4), (3, 5), (4, 5)])

G3 = nx.Graph()
G3.add_nodes_from(range(num_states))
G3.add_edges_from([(1, 3), (2, 0), (3, 4), (5, 6)])
graphs = [G1, G2, G3]
print(is_product_basis(graphs))

G1 = nx.Graph()
G1.add_nodes_from(range(num_states))
G1.add_edges_from([(0, 1), (0, 6), (2, 4), (5, 3)])

G2 = nx.Graph()
G2.add_nodes_from(range(num_states))
G2.add_edges_from([(0, 2), (0, 3), (0, 4), (0, 5), (1, 6)])

G3 = nx.Graph()
G3.add_nodes_from(range(num_states))
G3.add_edges_from([(0, 3), (0, 4), (1, 3), (1, 4), (6, 3), (6, 4), (2, 5)])
graphs = [G1, G2, G3]
print(is_product_basis(graphs))

orthog_graphs = construct_graph_relations(graphs)
from pprint import pprint

all_relations = []
for graph in orthog_graphs:
    nodes = graph.nodes

    relations = {}
    for node in nodes:
        neighbors = nodes[node].neighbors
        if tuple(neighbors) not in relations:
            relations[tuple(neighbors)] = [{node}]
        else:
            relations[tuple(neighbors)].append({node})

    for k, v in relations.items():
        relations[k] = set().union(*v)
    
    all_relations.append(relations)

#for relation in all_relations:
#    for k1, v1 in all_relations[0].items():
#        for k2, v2 in all_relations[1].items():
#            for k3, v3 in all_relations[2].items():
#                print(k1, k2, k3, v1, v2, v3)
#E = [dict(zip(all_relations.keys(), a)) for a in itertools.product(*all_relations.values())]
#print(E)
#shaded = list(itertools.product(*all_relations))
#print(shaded)
    #graph_relations = []
    #for k, v in relations.items():
    #    relations[k] = set().union(*v)
    #    graph_relations.append(set(k))
    #all_relations.append(graph_relations)

#shaded = list(itertools.product(*all_relations))


#for s in shaded:
#    if set().union(*s) == set(range(num_states)):


#print(sorted(set(graphs[0].edges) + set(graphs[1].edges)))

#p1 = graph_perms(G1)
#p2 = graph_perms(G2)
#p3 = graph_perms(G3)

#for g1 in p1:
#    for g2 in p2:
#        for g3 in p3:
#            print(is_upb([g1, g2, g3]))

#print(is_upb(graphs))

#all_graphs = generate_graphs('upb_search_s7_p4.txt')
#
#G1, G2, G3, G4 = all_graphs[7]
#
#x = graph_perms(G1)
#print(len(x))