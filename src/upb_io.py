"""Parse file format as generated by the QUPB_find_search.c file."""
import networkx as nx


def parse_file(filename: str) -> list[str]:
    """Parse each (possible) UPB in file."""
    with open(filename) as f:
        data = f.read()

    upbs = []
    for upb_data in data.split("UPB ")[1:]:
        upb_name, upb_data = upb_data.split(":\n")
        graphs = []
        for graph_data in upb_data.strip().split("\n"):
            edges = []
            for edge_data in graph_data.split(";"):
                endpoints = tuple(map(int, edge_data.split(",")))
                edges.append(endpoints)
            graphs.append(edges)
        upbs.append((upb_name, graphs))

    return upbs

def generate_graphs(filename: str) -> list[nx.Graph]:
    """Generates corresponding graphs of each parsed UPB."""
    upbs = parse_file(filename)
    all_graphs = {}
    for upb_name, upb_data in upbs:
        graphs = []
        for data in upb_data:
            graph_data = []
            for i in data:
                graph_data.append(nx.complete_bipartite_graph(i[0], i[1]))
            graphs.append(graph_data)
        all_graphs[upb_name] = graphs

    res = []
    for _, v in all_graphs.items():
        graphs = []
        for graph in v:
            graphs.append(nx.disjoint_union_all(graph))
        res.append(graphs)
    return res

#graphs = generate_graphs('upb_search_s7_p4.txt')
#print(len(graphs))