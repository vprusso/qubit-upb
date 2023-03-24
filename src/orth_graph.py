import itertools
import networkx as nx
import pandas as pd
pd.set_option("display.max_colwidth", None)


def get_properties(graph):
    nodes = {}
    for node in graph.nodes():
        neighbors = set([n for n in graph.neighbors(node)])
        reachable_nodes = set(nx.descendants(graph, node)) - set(neighbors)
        nodes[node] = {
            "neighbors": neighbors,
            "reachable_nodes": reachable_nodes,
        }
    return pd.DataFrame.from_dict(nodes).transpose()


def get_shaded_region(graph):
    df = get_properties(graph)
    df["neighbors"] = df["neighbors"].apply(frozenset)

    # group the dataframe by "neighbors" and get the corresponding indices
    grouped = df.groupby("neighbors").agg(list)

    # reset the index and get the "neighbors" column as a list
    grouped = grouped.reset_index()["neighbors"].tolist()

    shaded_regions = []
    # print the unique sets of "neighbors" along with the corresponding indices
    for neighbors in grouped:
        # indices = df.index[df["neighbors"] == neighbors].tolist()
        shaded_regions.append(set(neighbors) )
        # shaded_regions[neighbors] = indices
    return shaded_regions


def is_unextendible(graphs: list[nx.Graph]) -> bool:
    """Check if set of orthogonality graphs are extendible.

    A set of orthogonality graphs are extendible if we can find a product state
    that is orthogonal to the all the states amongst the graphs.
    """
    # Corollary of Lemma 2 in arXiv:1302.1604: In the orthogonality graph of a
    # UPB, every party must have an even number of distinct shaded regions.
    shaded_regions = []
    for graph in graphs:
        shaded_region = get_shaded_region(graph)
        if len(shaded_region) % 2 != 0:
            return False
        shaded_regions.append(shaded_region)
    
    # A set of product states is unextendible if and only if there is no way to
    # choose one shaded region on each parry such that every vertex is contained
    # within at least one of the shaded regions.
    combinations = list(itertools.product(*shaded_regions))
    for comb in combinations:
        all_sets = set().union(*comb)
        if all_sets == set(range(len(graph.nodes))):
            return False
    return True


def is_product_basis(graphs: list[nx.Graph]) -> bool:
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


def is_upb(graphs: list[nx.Graph]) -> bool:
    """Check if set of orthogonality graphs form an unextendible product basis."""
    if is_product_basis(graphs) and is_unextendible(graphs):
        return True
    return False


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

print(is_unextendible(graphs))
