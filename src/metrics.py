# -----------------------------------------------------------------------------
# Author: Camilo Chacón Sartori
# Date: 17-10-2024
#
# This file is part of OptiPattern.
#
# Copyright (c) [2024] Camilo Chacón Sartori

import networkx as nx

def format_scientific_notation(x):
    if x == 0:
        return "0"
    else:
        return "{:.0e}".format(x)
       
def calculate_metrics(path_graph):
    G = nx.DiGraph()
    G_pagerank = nx.DiGraph()
    with open(path_graph, 'r') as f:
        for line in f.readlines():
            n1, n2 = line.split()
            G.add_edge(n1, n2)
    
    G_reversed = G.reverse(copy=True)

    in_degree_centrality = nx.in_degree_centrality(G)
    out_degree_centrality = nx.out_degree_centrality(G)
    closeness_centrality = nx.closeness_centrality(G_reversed)
    betweenness_centrality = nx.betweenness_centrality(G, endpoints=True)
    pagerank = nx.pagerank(G_reversed)
    degrees = nx.degree(G)

    metrics = []
    for node in sorted(G.nodes(), key=lambda x: int(x)):
        idc = format_scientific_notation(in_degree_centrality[node]/max(in_degree_centrality.values()))
        odc = format_scientific_notation(out_degree_centrality[node]/max(out_degree_centrality.values()))
        cc = format_scientific_notation(closeness_centrality[node]/max(closeness_centrality.values()))
        bc = format_scientific_notation(betweenness_centrality[node]/max(betweenness_centrality.values()))
        pr = format_scientific_notation(pagerank[node]/max(pagerank.values()))
        metrics.append([node, idc, odc, cc, bc, pr])

    results = [",".join(map(str, sublist)) for sublist in metrics]
    return "\n".join(results)
        